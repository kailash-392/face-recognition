import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image1.jpg','Kailash'),
      ('image2.jpg','Elon Musk'),
      ]
  
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('topys-images','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
