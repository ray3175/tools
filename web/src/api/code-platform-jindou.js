import axios from 'axios';
import { AUTH } from "@/config/auth";
import { CODE_PLATFORM } from "@/config/code-platform";
import { CODE_PLATFORM_JINDOU } from "@/config/code-platform-info";


const loginJinDou = function (user, password, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_JINDOU.url + CODE_PLATFORM_JINDOU.uri.login,
        params: {
            userName: user,
            password: password
        }
    }, {
        headers: headers
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};

const getBalanceJinDou = function (_token, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_JINDOU.url + CODE_PLATFORM_JINDOU.uri.balance,
        params: {
            token: _token
        }
    }, {
        headers: headers
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};

const getPhoneNumberJinDou = function (_token, item, type, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    if (type === "0") {
        type = "exclude4";
    } else if (type === "1") {
        type = "unlimit";
    } else if (type === "2") {
        type = "include2";
    } else if (type === "3") {
        type = "include3";
    } else if (type === "4") {
        type = "include1";
    } else if (type === "5") {
        type = "include4";
    }
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_JINDOU.url + CODE_PLATFORM_JINDOU.uri.phone,
        params: {
            token: _token,
            sid: item,
            operator: type
        }
    }, {
        headers: headers
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};

const getSelfDefinePhoneNumberJinDou = function (_token, item, type, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_JINDOU.url + CODE_PLATFORM_JINDOU.uri.selfDefinePhone,
        params: {
            token: _token,
            sid: item,
            phone: type
        }
    }, {
        headers: headers
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};

const releasePhoneNumberJinDou = function (_token, item, phone=null, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_JINDOU.url + CODE_PLATFORM_JINDOU.uri.releasePhone,
        params: {
            token: _token,
            sid: item,
            phone: phone
        }
    }, {
        headers: headers
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};

const removePhoneNumberJinDou = function (_token, item, phone=null, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_JINDOU.url + CODE_PLATFORM_JINDOU.uri.removePhone,
        params: {
            token: _token,
            sid: item,
            phone: phone
        }
    }, {
        headers: headers
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};

const getMessageJinDou = function (_token, item, phone=null, successCall=null, errorCall=null) {
    let token = CODE_PLATFORM.key;
    let auth = localStorage.getItem(AUTH.key);
    let headers = {};
    headers[token] = auth;
    axios.post(CODE_PLATFORM.url + CODE_PLATFORM.uri.repost, {
        url: CODE_PLATFORM_JINDOU.url + CODE_PLATFORM_JINDOU.uri.getMessage,
        params: {
            token: _token,
            sid: item,
            phone: phone
        }
    }, {
        headers: headers
    }).then((rsp) => {
        if (successCall) {
            successCall(rsp);
        } else {
            return rsp;
        }
    }).catch((error) => {
        if (errorCall) {
            errorCall(error);
        } else {
            alert("服务器连接失败！");
        }
    })
};


export {
    loginJinDou,
    getBalanceJinDou,
    getPhoneNumberJinDou,
    getSelfDefinePhoneNumberJinDou,
    releasePhoneNumberJinDou,
    removePhoneNumberJinDou,
    getMessageJinDou
};
