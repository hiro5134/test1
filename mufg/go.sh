git pull

git add .

today=`date "+%m/%d/%Y %T"`
now="by GCP at ${today}"
git commit -m "${now}"

git push
