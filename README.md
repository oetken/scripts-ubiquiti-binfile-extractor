# scripts-ubiquiti-binfile-extractor

I used this to flash the stock firmware of my Ubiquity Unifi U6 LR.
The recovery did not work but with openwrt still running I could flash the mtd partions of the stock firmware after extracting them with the script.
SSH into openwrt.
```bash
cat /proc/mtd
mtd0: 00080000 00010000 "u-boot"
mtd1: 00010000 00010000 "partition-table"
mtd2: 00010000 00010000 "product-info"
mtd3: 00cf0000 00010000 "firmware"
mtd4: 002a0000 00010000 "kernel"
mtd5: 00a50000 00010000 "rootfs"
mtd6: 00650000 00010000 "rootfs_data"
mtd7: 00060000 00010000 "user-config"
mtd8: 00080000 00010000 "mutil-log"
mtd9: 00040000 00010000 "oops"
mtd10: 00010000 00010000 "radio"

mtd write <part>.mtd /dev/mtd<use from list>
```
