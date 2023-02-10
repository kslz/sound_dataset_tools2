# -*- coding: utf-8 -*-
"""
    @Time : 2023/2/9/009 17:15
    @Author : 李子
    @Url : https://github.com/kslz
"""
import sqlite3

from utils.log import creatlogger


class MyDB():
    def __init__(self, path="db/data.db"):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        self.sqlitelogger = creatlogger("sqlitelogger")
        self.sqlitelogger.debug("数据库连接已启动")

    def init_database(self):
        self.create_workspace_tbl()
        pass

    def create_workspace_tbl(self):
        self.cur.execute('''CREATE TABLE "workspace_tbl" (
              "workspace_name" TEXT,
              "workspace_create_time" TEXT,
              "workspace_last_use_time" TEXT,
              "workspace_info" TEXT
            );''')
        self.sqlitelogger.debug("新建工作区表")
        self.con.commit()

    def create_dataset_tbl(self):
        self.cur.execute('''CREATE TABLE "dataset_tbl" (
              "dataset_id" INTEGER NOT NULL,
              "dataset_name" TEXT,
              "dataset_create_time" TEXT,
              "dataset_last_use_time" TEXT,
              "dataset_info" TEXT,
              PRIMARY KEY ("dataset_id")
            );''')
        self.sqlitelogger.debug("新建数据集表")
        self.con.commit()
