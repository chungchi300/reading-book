echo -e "Hi, please type the short_message for commit: "
read  short_message
git stash
git pull
git stash pop
git add -A
git commit -m $short_message
git push
echo -e "Commit & push done,have a nice day"
