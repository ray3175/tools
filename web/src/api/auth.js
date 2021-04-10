import axios from 'axios';
import { AUTH } from "@/config/auth";


const getHashAccount = function (account, password, successCall=null, errorCall=null) {
    axios.post(AUTH.url + AUTH.uri.authAccount, {
        account: account,
        password: password
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

const getAccountInfo = function (hashAccount, successCall=null, errorCall=null) {
    axios.post(AUTH.url + AUTH.uri.auth, {
        "xy-auth": hashAccount
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

const registerAccount = function (account, password, idCard, name, phone, mail, successCall=null, errorCall=null) {
    axios.post(AUTH.url + AUTH.uri.user, {
        account: account,
        password: password,
        id_card: idCard,
        name: name,
        phone: phone,
        mail: mail
    }, {
        headers: {
            project_name: AUTH.projectName,
            project_auth_code: AUTH.projectAuthCode
        }
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


export { getHashAccount, getAccountInfo, registerAccount };
