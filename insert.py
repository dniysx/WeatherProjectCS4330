import pymysql

db = pymysql.connect("localhost", "weather", "weather", "weather")

cursor = db.cursor()

def insertStation(stationid, name, state, lat, long, elev):
    insert = "INSERT INTO STATION(StationID, Name, State, Latitude, Longitude, Elevation)\
    VALUES('%s','%s', '%s', %f, %f, %d)" % (stationid, name, state, lat, long, elev)
    
    try:
        cursor.execute(insert)
        db.commit()
    except:
        print('Failed')
        db.rollback()
        
def insertPrecip(stationid, date, precip, snow, snow_depth):
    insert = "INSERT INTO Precipitation(StationID, Date, Precip, Snowfall, SnowDepth)\
    VALUES('%s','%s', %f, %f, %f)" %(stationid, date, precip, snow, snow_depth)
    
    try:
        cursor.execute(insert)
        db.commit()
    except:
        print('Failed')
        db.rollback()
        
def insertTemp(stationid, date, AvgTemp, MaxTemp, MinTemp, ObsTemp):
    insert = "INSERT INTO Temperature(StationID, Date, AvgTemp, MaxTemp, MinTemp, ObsTemp)\
    VALUES('%s', '%s', %f, %f, %f,%f)" % (stationid, date, AvgTemp, MaxTemp, MinTemp, ObsTemp)
    print(insert)
    try:
        cursor.execute(insert)
        db.commit()
    except:
        print('Failed')
        db.rollback()

def insertWind(stationid, date, avgwind, fast2, fast5, peakgustspd, fastmilespd):
    insert = "INSERT INTO Wind(StationID, Date, AvgWindSpd, Fastest2Min, \
                Fastest5Sec, PeakGustSpd, FastestMileSpd)\
    VALUES('%s','%s', %f, %f, %f, %f, %f)" % (stationid, date,  avgwind, fast2, fast5, peakgustspd, fastmilespd)
    
    try:
        cursor.execute(insert)
        db.commit()
    except:
        print('Failed')
        db.rollback()
        
insertStation('test', 'test', 'te', 45.000, -135.000, 12)   
station = 'test'
date = '3000-11-01'
avg = 32.2
maxt = 99
mint = -45
obst = 45
insertTemp(station, date, avg, maxt, mint, obst)

db.close()