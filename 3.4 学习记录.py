# 1.from datetime import datetime 或import datetime.datetime
# 2.获取当前时间：datetime.now()
#   指定时间：dt=datetime(2020, 5, 12 ,9, 45) >>> 200-05-12 09:45:00
# 3.epch time记为0，1970-01-01 00:00:00 UTC+00:00时区时刻
# 4.转换：datetime(time).timestamp() >>> 秒.毫秒 class<float>
# 5.本地时间：datetime.fromtimestamp(距离epch time秒)
#   格林威治时间：datetime.utcfromtimestamp(距离epch time秒)
# 6.str转换为datetime：转换后的datetime没有时区属性
#   datetime.strptime('2020-6-1 19:45:27','%Y-%m-%d %H:%M:%S')
# 7.datetime转换为str:
#   datetime.now().strftime('%a,%b %d %H:%M')
# 8.datetime加减，需导入timedelta类：time+timedelta(days=, hours=)
# 9.本地时间转换为UTC时间：
#   导入timezone类，利用tzinfo(默认None)属性
#   创建时区UTC+8:00 tz_utc_8=timezone(timedelta(hours=8))
#   强制设置为UTC+8:00 now.replace(tzinfo=tz_utc_8)
#10.时区转换：
#   先拿datetime时间，utc_time=datetime.utcnow().replace(tzinfo=timezone.utc)
#   bj_time=utc_time.astimezone(timezone(timedelta(hours=8)))
#11.%a/%A:星期 %b/%B:月份(英) %m:月 %y/%Y:年份 %I/%H:小时 %M/%S:分秒