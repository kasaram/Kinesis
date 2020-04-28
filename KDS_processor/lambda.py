import base64
from aws_kinesis_agg.deaggregator import deaggregate_records


def lambda_handler(event, context):
    """
    lambda handler reads records put on the kinesis data stream. Records are aggregated,
    so are manually deaggregated

    records are recieved as base64 encoded string. Decoding them returns a bytes string 
    which is further decoded to get the actual string object

    :param event:  the event object generated by the service invoked
    :param context: This object provides methods and properties that provide information about the invocation, function\
    and execution environment.
    :return: none
    """

    aggregated_kinesis_records = event['Records']
    deaggregated_records = deaggregate_records(aggregated_kinesis_records)

    for record in deaggregated_records:
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        print("Decoded payload: ", payload)

        # custom processing on payload here

        return 'Successfully processed {} records.'.format(len(aggregated_kinesis_records))