git pull

git add .

today=`date "+%m/%d/%Y %T"`
now="by GCP at ${today}"
git commit -m "${now}"

git push

if [ "$1" -eq 1 ]; then
	sudo shutdown -h now
else
	echo "continue"
fi
