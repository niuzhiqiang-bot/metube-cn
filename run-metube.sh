#!/usr/bin/env bash
# MeTube 启动脚本（大阪 osaka-arm / 161.33.40.15）
# 用途：容器被删/重建时，用本脚本按原配置重新拉起。
# 用法：bash ~/metube/run-metube.sh
set -euo pipefail

# cookies 文件位于挂载卷内，容器重建后仍然有效
# DELETE_FILE_ON_TRASHCAN=ask: 前端删除条目时同步删除磁盘文件
sudo docker run -d \
  --name metube \
  --restart unless-stopped \
  -p 127.0.0.1:8081:8081 \
  -v /var/www/downloads:/downloads \
  -e 'YTDL_OPTIONS={"cookiefile":"/downloads/cookies.txt"}' \
  -e DELETE_FILE_ON_TRASHCAN=ask \
  metube-cn:2026.10.20

echo "meTube started; check: docker ps --filter name=metube"
