const CODE_PLATFORM_KEKE = {
    website: "http://www.hfsxf.com:81/index.html",
    name: "可可接码平台",
    describe: "验证码接码平台！",
    url: "http://dkh.hfsxf.com:81",
    uri: {
        login: "/service.asmx/UserLoginStr",            // 登录接口
        balance: "/service.asmx/GetBalanceStr",         // 获取金额接口
        phone: "/service.asmx/GetHMStr",                // 获取号码接口
        releasePhoneAll: "/service.asmx/sfAllStr",      // 释放所有号码
        releasePhone: "/service.asmx/sfHmStr",          // 释放指定号码
        removePhone: "/service.asmx/HmdStr",            // 拉黑指定号码
        getMessage: "/service.asmx/GetYzmStr"           // 获取短信
    },
    item: {
        "巧虎": 1717
    }
};

const CODE_PLATFORM_JINDOU = {
    website: "http://www.92jindou.com",
    name: "筋斗云接码平台",
    describe: "验证码接码平台！",
    url: "http://openapi.92jindou.com",
    uri: {
        login: "/api/login",                            // 登录接口
        balance: "/api/getSummary",                     // 获取金额接口
        phone: "/api/getPhone",                         // 获取号码接口
        selfDefinePhone: "/api/specified",              // 获取指定号码接口
        releasePhone: "/api/cancelRecv",                // 释放号码
        removePhone: "/api/addBlacklist",               // 拉黑指定号码
        getMessage: "/api/getMessage"                   // 获取短信
    },
    item: {
        "巧虎": 4439
    }
};

const CODE_PLATFORM_MIYI = {
    website: "http://www.wkxudxec.cn",
    name: "米宜接码平台",
    describe: "验证码接码平台！",
    url: "http://www.wkxudxec.cn",
    uri: {
        login: "/api/login",                            // 登录接口
        balance: "/api/getSummary",                     // 获取金额接口
        phone: "/api/getPhone",                         // 获取号码接口
        selfDefinePhone: "/api/specified",              // 获取指定号码接口
        releasePhone: "/api/cancelRecv",                // 释放号码
        removePhone: "/api/addBlacklist",               // 拉黑指定号码
        getMessage: "/api/getMessage"                   // 获取短信
    },
    item: {
        "巧虎": 991
    }
};


export { CODE_PLATFORM_KEKE, CODE_PLATFORM_JINDOU, CODE_PLATFORM_MIYI };
