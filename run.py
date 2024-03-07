import numpy as np

def gold(input_file, planogram_type) -> (str): 
    import json
    import logging
    import uuid
    logging.getLogger().setLevel(logging.INFO)

    import cv2
    import numpy as np

    from cognitive_service_vision_model_customization_python_samples import ResourceType
    from cognitive_service_vision_model_customization_python_samples.clients import PlanogramComplianceClient, ProductRecognitionClient
    from cognitive_service_vision_model_customization_python_samples.models import PlanogramMatchingRequest, ProductRecognition
    from cognitive_service_vision_model_customization_python_samples.tools import visualize_matching_result, visualize_planogram

    # Resource and key
    resource_type = ResourceType.SINGLE_SERVICE_RESOURCE # or ResourceType.MULTI_SERVICE_RESOURCE

    resource_name = None
    multi_service_endpoint = None

    if resource_type == ResourceType.SINGLE_SERVICE_RESOURCE:
        resource_name = 'Fonterra-Vision-Instance'
        assert resource_name
    else:
        multi_service_endpoint = '{specify_your_service_endpoint}'
        assert multi_service_endpoint

    resource_key = '882311aa18cf43e58fe25901b28e018e'

    planogram = json.load(open(f'static/Resources/Planograms/JSONs/{planogram_type}', 'r'))
    print("\nPlanogram Loaded Successfully.")

    client = ProductRecognitionClient(resource_type, resource_name, multi_service_endpoint, resource_key)
    run_name = str(uuid.uuid4())
    # model_name = 'ms-pretrained-product-detection'
    model_name = 'fonterramodel01'

    print("\nModel is Running...\n")
    run = ProductRecognition(run_name, model_name)

<<<<<<< HEAD
    print('printing run\n')

    print(run)

=======
>>>>>>> 39cb21033c2c1a9aed639d074fa8a589b7a5c2cd
    with open(f'static/Uploads/{input_file}', 'rb') as f:
        img = f.read()

    try:
        client.create_run(run, img, 'image/png')
        recognition_result = client.wait_for_completion(run_name, model_name)
    finally:
        client.delete_run(run_name, model_name)

<<<<<<< HEAD
    print('\nrecognition_result : \n')
    print(recognition_result)

=======
>>>>>>> 39cb21033c2c1a9aed639d074fa8a589b7a5c2cd
    client = PlanogramComplianceClient(resource_type, resource_name, multi_service_endpoint, resource_key)
    matching_request = PlanogramMatchingRequest(recognition_result.result, planogram)
    matching_result = client.match_planogram(matching_request)

    cv_img = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_COLOR)
    json_out = visualize_matching_result(cv_img, matching_result.to_dict(), planogram)

    # cv2.imwrite(f'C:/Users/malit/Documents/DXDY/web-app-mui/public/matching_result.jpg', cv_img)
    return json_out