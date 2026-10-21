#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MeTube 界面汉化脚本：对 Angular 打包产物 main-*.js 做中文本地化替换。

MeTube 官方前端无 i18n 框架，界面文字在 Angular 编译产物中以
C(<id>,"<英文>") 形式硬编码。本脚本精确匹配该结构，将英文替换为中文，
保留 MeTube/GitHub/yt-dlp/URL/Cookie 等专有名词。运行后生成中文界面。

注：非 ASCII 字符（如不换行空格 \\xA0、省略号 \\u2026）在打包产物中以
字面转义文本存在，因此源串使用对应的字面转义形式匹配。
"""
import glob
import os
import re

# (英文原文, 中文译文)。英文原文保持打包产物中的字面形式。
MAP = [
    ("Select all", "全选"),
    ("Select item", "选择项目"),
    (" Browse ", " 浏览 "),
    ("Loading entries\\u2026", "正在加载条目…"),
    ("No entries found.", "未找到条目"),
    ("Downloaded", "已下载"),
    ("Title", "标题"),
    ("Duration", "时长"),
    (" Cancel ", " 取消 "),
    ("Check all now ", "立即全部检查 "),
    ("\\xA0 Check all now ", " 立即全部检查 "),
    ("Check selected ", "检查所选 "),
    ("\\xA0 Check selected ", " 检查所选 "),
    ("Save", "保存"),
    ("Edit", "编辑"),
    ("Active", "运行中"),
    ("Paused", "已暂停"),
    ("\\xA0 Delete selected ", " 删除所选 "),
    ("Name", "名称"),
    ("Filter", "筛选"),
    ("Interval (min)", "间隔(分钟)"),
    ("Last checked", "上次检查"),
    ("Status", "状态"),
    ("Subscriptions", "订阅"),
    ("Cancel Import", "取消导入"),
    ("Batch Import URLs", "批量导入链接"),
    ("Close", "关闭"),
    (" Import URLs ", " 导入链接 "),
    ("LIVE", "直播"),
    ("Queued", "排队中"),
    (" Waiting for stream ", " 等待直播流 "),
    ("Post-processing", "后处理中"),
    ("\\xA0 Cancel selected", " 取消所选"),
    ("\\xA0 Download selected", " 下载所选"),
    ("Video", "视频"),
    ("Format", "格式"),
    ("Speed", "速度"),
    ("ETA", "剩余时间"),
    ("Downloading", "下载中"),
    ("Click for details ", "点击查看详情 "),
    ("Message:", "消息："),
    ("Error:", "错误："),
    ("Copied!", "已复制！"),
    ("URL:", "链接："),
    ("\\xA0 Clear selected", " 清空所选"),
    ("\\xA0 Clear completed", " 清空已完成"),
    ("\\xA0 Clear failed", " 清空失败"),
    ("\\xA0 Retry failed", " 重试失败"),
    ("\\xA0 Download Selected", " 下载所选"),
    ("Type", "类型"),
    ("Quality", "画质"),
    ("Codec / Format", "编码/格式"),
    ("File Size", "文件大小"),
    ("Completed", "已完成"),
    (" Canceling... ", " 正在取消… "),
    (" Adding... ", " 正在添加… "),
    (" Download ", " 下载 "),
    ("More download actions", "更多下载操作"),
    (" Subscribing... ", " 正在订阅… "),
    (" Browse\\u2026 ", " 浏览… "),
    (" Subscribe ", " 订阅 "),
    ("Codec", "编码"),
    ("Tags", "标签"),
    ("Language", "语言"),
    ("Subtitle Source", "字幕来源"),
    ("Template", "模板"),
    ("Clip start", "片段开始"),
    ("Clip end", "片段结束"),
    ("Custom yt-dlp Options", "自定义 yt-dlp 选项"),
    (" Cookies active ", " 已启用 Cookies "),
    (" No cookies configured ", " 未配置 Cookies "),
    (" Connecting to server... ", " 正在连接服务器… "),
    ("yt-dlp-options", "yt-dlp 选项"),
    (" Advanced Options ", " 高级选项 "),
    ("Output", "输出"),
    ("Download Folder", "下载目录"),
    ("Custom Name Prefix", "自定义文件名前缀"),
    ("Remove sponsor segments", "移除赞助商片段"),
    ("Split by chapters", "按章节拆分"),
    ("Behavior", "行为"),
    ("Auto Start", "自动开始"),
    ("Yes", "是"),
    ("No", "否"),
    ("Items Limit", "条目数量限制"),
    ("Subscription Check (min)", "订阅检查间隔(分钟)"),
    ("Subscription Title Filter", "订阅标题筛选"),
    ("Skip members-only subscription videos", "跳过仅会员可见的视频"),
    ("Option Presets", "预设选项"),
    ("Video Password", "视频密码"),
    ("Tools", "工具"),
    ("Cookies", "Cookies"),
    ("Bulk Actions", "批量操作"),
    (" Export URLs ", " 导出链接 "),
    (" Copy URLs ", " 复制链接 "),
]


def main() -> None:
    targets = glob.glob("/app/ui/dist/metube/browser/main-*.js")
    if not targets:
        print("ERROR: 未找到 main-*.js")
        raise SystemExit(1)
    replaced = 0
    for f in targets:
        with open(f, encoding="utf-8") as fh:
            t = fh.read()
        for en, zh in MAP:
            pat = re.compile(r'(C\(\d+,")' + re.escape(en) + r'("\))')
            t, n = pat.subn(lambda m: m.group(1) + zh + m.group(2), t)
            replaced += n
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(t)
        print(f"已处理 {os.path.basename(f)}，共替换 {replaced} 处")


if __name__ == "__main__":
    main()
