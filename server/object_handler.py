import boto3
from rekognition_image import RekognitionImage

class ObjectDetector:
    """
        Represents one Amazon rekognition object detection call and the response of it.
        Raises botocore.exceptions.ClientError if API call to Rekognition fails.
    """

    def __init__(self, payload, img_name):
        rekognition_client = boto3.client('rekognition')
        self.rekog_obj = RekognitionImage(
            {'Bytes': payload}, img_name, rekognition_client)

        print("Analyzing objects............")
        self.obj_meta_data = self.rekog_obj.detect_labels(5)

        print("object detection data:: ", self.obj_meta_data)

        print(f"Found {len(self.obj_meta_data)} object")
        for obj in self.obj_meta_data:
            print("Object Label:: ", obj.to_dict())

        if len(self.obj_meta_data) < 1:
            raise FileNotFoundError("No Objects present in the given Image.")

