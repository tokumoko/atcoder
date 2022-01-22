cd C:\Users\ic201229\github\atcoder
git init
git config --global user.name "tokumoko"
git config --global user.email "c.haruto.2727@gmail.com"
git clone https://github.com/tokumoko/atcoder C:\Users\ic201229\github\atcoder\atcoder
xcopy /d C:\Users\ic201229\Desktop\vscode program\project\list3\kyoupro C:\Users\ic201229\github\atcoder\atcoder
cd atcoder
git add --all
git commit -m "auto commit"
git push -f
exit
