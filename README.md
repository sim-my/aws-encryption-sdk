### Steps to run this repository locally

<ol>
  <li>Create a virtual environment venv: <strong>python3 -m venv venv</strong></li>
  <li>Activate your virtual environment: <strong>source venv/bin/activate</strong></li>
  <li>Install everything from <strong>requirement.txt</strong>: <strong>pip3 install -r requirement.txt</strong></li>
  <li>Make a copy of <strong>.testEnv</strong> as <strong>.env</strong></li>
  <li>Populate environment variables of <strong>AWS_ACCESS_KEY_ID</strong> and <strong>AWS_SECRET_ACCESS_KEY</strong></li>
  <li>Create a key in <strong>AWS KMS</strong> and copy its <strong>ARN</strong> and populate in <strong>.env</strong> at <strong>ENCRYPTION_KEY_ID</strong></li>
  <li>Create a bucket in <strong>AWS S3</strong> and populate in <strong>.env</strong> file at <strong>BUCKET_NAME</strong></li>
  <li>Run <strong>main.py</strong>: <strong>python3 ./main.pyfile</strong></li>
</ol>

### AWS Services Used

<ol>
  <li>AWS S3</li>
  <li>AWS KMS</li>
  <li>AWS Encryption SDK for Python</li>
</ol>
    
