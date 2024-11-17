# misis_tuda_syuda
## BIV hack challenge

```
git clone https://github.com/AlexxxGorin/biv-hack.git
```
```
docker build -t turbo_bert_inference . 
```
```
docker run --rm -v $(pwd):/data turbo_bert_inference /data/payments_main.tsv /data/output.tsv
```
