import pytest

from detect_secrets.plugins.ibm_cloud_iam import IBMCloudIAMDetector


CLOUD_IAM_KEY = 'abcd1234abcd1234abcd1234abcd1234abcd1234--__'


class TestIBMCloudIamDetector:

    @pytest.mark.parametrize(
        'payload, should_flag',
        [
            ('ibm-cloud_api_key: {cloud_iam_key}'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('ibm_cloud_iam-key : {cloud_iam_key}'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('IBM-API-KEY : "{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('"iam_api_key" : "{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('cloud-api-key: "{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('"iam-password": "{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('CLOUD_IAM_API_KEY:"{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('ibm-cloud-key:{cloud_iam_key}'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('ibm_key:"{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            (
                '"ibm_cloud_iam_api_key":"{cloud_iam_key}"'.format(
                    cloud_iam_key=CLOUD_IAM_KEY,
                ), True,
            ),
            ('ibm_cloud_iamapikey= {cloud_iam_key}'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('ibm_cloud_api_key= "{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('IBMCLOUDIAMAPIKEY={cloud_iam_key}'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('cloud_iam_api_key="{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('ibm_api_key := {cloud_iam_key}'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('"ibm-iam_key" := "{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            (
                '"ibm_cloud_iam_api_key":= "{cloud_iam_key}"'.format(
                    cloud_iam_key=CLOUD_IAM_KEY,
                ), True,
            ),
            ('ibm-cloud_api_key:={cloud_iam_key}'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('"cloud_iam_api_key":="{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('ibm_iam_key:= "{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True,),
            ('ibm_api_key:="{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True),
            ('ibm_password = "{cloud_iam_key}"'.format(cloud_iam_key=CLOUD_IAM_KEY), True),
            ('ibm-cloud-pwd = {cloud_iam_key}'.format(cloud_iam_key=CLOUD_IAM_KEY), True),
            ('iam_api_key="%s" % IBM_IAM_API_KEY_ENV', False),
            ('CLOUD_APIKEY: "insert_key_here"', False),
            ('cloud-iam-key:=afakekey', False),
            ('fake-cloud-iam-key= "not_long_enough"', False),
        ],
    )
    def test_analyze_string(self, payload, should_flag):
        logic = IBMCloudIAMDetector()

        output = logic.analyze_string(payload, 1, 'mock_filename')
        assert len(output) == (1 if should_flag else 0)
