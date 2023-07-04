# Dragon-tales

A web app focused on dynamically generating random stories as per users prompt.

# Features
- Randomly generate stories on a click of a button!
- Generate your personalised stories with the help of chatGPT.
- Store your collection of stories and read it again.
- 

docker build -t gcr.io/dragon-tales-frontend/dragontaleapp:UI .

docker push gcr.io/dragon-tales-frontend/dragontaleapp:UI

gcloud run deploy --image gcr.io/dragon-tales-frontend/dragontaleapp:UI --platform managed

GCP

===
clone the app

cd to thr folder

export \
    PROJECT_ID=dragon-tales-frontend


gcloud artifacts locations list

export REGION=us-west1

gcloud artifacts repositories \
    create dragon-tales-repo \
    --repository-format=docker \
    --location=${REGION} \
    --description="Docker \
    repository"


docker build -t \
    ${REGION}-docker.pkg.dev/${PROJECT_ID}/dragon-tales-repo/dragontaleapp:UI \
    .

gcloud services enable \
    artifactregistry.googleapis.com


gcloud auth configure-docker \
    ${REGION}-docker.pkg.dev

docker push \
    ${REGION}-docker.pkg.dev/${PROJECT_ID}/dragon-tales-repo/dragontaleapp:UI


https://cloud.google.com/kubernetes-engine/docs/how-to/automated-deployment?authuser=5

