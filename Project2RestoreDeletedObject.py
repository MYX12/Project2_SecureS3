import json
import boto3

s3 = boto3.client('s3')

# 源桶（恢复桶）
RECOVERY_BUCKET = "project2-recover-bucket"
# 目标桶（被删除的对象所在的主桶）
TARGET_BUCKET = "sensitive-data-secured-bucket"

def lambda_handler(event, context):
    print("===DeleteObject Event Triggered===")
    print(json.dumps(event, indent=4))

    try:
        records = event.get("detail", {}).get("requestParameters", {})
        object_key = records.get("key")
        bucket_name = records.get("bucketName")

        # 验证是否是主桶上的操作
        if bucket_name != TARGET_BUCKET:
            print(f"Ignoring deletion from unrelated bucket: {bucket_name}")
            return {
                'statusCode': 200,
                'body': json.dumps('Event ignored.')
            }

        print(f"Restoring deleted object: {object_key}")

        # 从恢复桶复制对象回主桶
        s3.copy_object(
            Bucket=TARGET_BUCKET,
            Key=object_key,
            CopySource={'Bucket': RECOVERY_BUCKET, 'Key': object_key}
        )

        print("Object restored successfully.")
        return {
            'statusCode': 200,
            'body': json.dumps(f"{object_key} restored successfully.")
        }

    except Exception as e:
        print("Error restoring object:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps("Failed to restore object.")
        }
