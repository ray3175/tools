const getDate = function (year=0, month=0, day=0, hour=0, minute=0, second=0) {
    let dateObj = new Date();
    let timeDifference = null;
    if (year) {
        timeDifference = dateObj.getFullYear() + year;
    }
    if (month) {
        timeDifference = dateObj.getMonth() + month;
    }
    if (day) {
        timeDifference = dateObj.getDate() + day;
    }
    if (hour) {
        timeDifference = dateObj.getHours() + hour;
    }
    if (minute) {
        timeDifference = dateObj.getMinutes() + minute;
    }
    if (second) {
        timeDifference = dateObj.getSeconds() + second;
    }
    if (timeDifference) {
        dateObj.setDate(timeDifference);
    }
    return {
        year: dateObj.getFullYear(),
        month: dateObj.getMonth() + 1,
        day: dateObj.getDate(),
        hours: dateObj.getHours(),
        minutes: dateObj.getMinutes(),
        seconds: dateObj.getSeconds()
    };
};

const getDateString = function (year=0, month=0, day=0, hour=0, minute=0, second=0) {
    const dateDict = getDate(year, month, day, hour, minute, second);
    return date2string(dateDict);
};

const date2string = function (dateDict) {
    function getDateValue (value) {
        if (value < 10) {
            value = "0" + value;
        }
        return value;
    }
    let month = getDateValue(dateDict.month);
    let day = getDateValue(dateDict.day);
    let hours = getDateValue(dateDict.hours);
    let minutes = getDateValue(dateDict.minutes);
    let seconds = getDateValue(dateDict.seconds);
    return dateDict.year + "-" + month + "-" + day + " " + hours + ":" + minutes + ":" + seconds;
};


export { getDate, getDateString };
