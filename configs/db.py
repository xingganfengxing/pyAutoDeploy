#coding=utf-8
from configs import setting

__author__ = '华帅'

DB = setting.CUR_DIR % 'db'

CREATE_JOB_SQL = 'create table tb_job (id integer primary key autoincrement, name varchar(100), dir varchar(100), ' \
                 'url varchar(500), exe_time datetime, status varchar(10));'
CREATE_LOG_SQL = 'create table tb_log (id integer primary key autoincrement, ' \
                 'job_id integer, exe_time varchar(19), statue varchar(10), content text);'
CREATE_QUEUE_SQL = 'create table tb_queue (id integer primary key autoincrement, job_id integer, job_name varchar(100));'

INSERT_TO_JOB = 'insert into tb_job (status, name, dir, url) values ("%s", "%s", "%s", "%s");'
DELETE_JOB = 'delete from tb_job where id = %d;'
SELECT_DIR_FROM_JOB_BY_ID = 'select dir, name, id from tb_job where id = %d;'
SELECT_DIR_FROM_JOB_BY_URL = 'select dir, name, id from tb_job where url = "%s";'

UPDATE_JOB = 'update tb_job set status = "%s", exe_time = "%s" where id = %d'