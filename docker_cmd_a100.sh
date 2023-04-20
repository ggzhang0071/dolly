img="nvcr.io/nvidia/pytorch:23.01-py3"



sudo docker run --gpus all  --privileged=true   --workdir /git --name "dolly"  -e DISPLAY --ipc=host -d --rm  -p 6327:4352  \
-v /localhome/local-vili/git/dolly:/git/dolly \
 -v /localhome/local-vili/git/datasets:/git/datasets \
 $img sleep infinity


sudo docker exec -it dolly  /bin/bash


