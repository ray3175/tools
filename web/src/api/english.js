import axios from 'axios';
import { AUTH } from "@/config/auth";
import { ENGLISH } from "@/config/english";


const authVerify = function (gotoLogin, successCall=null, errorCall=null) {
    let token = ENGLISH.key;
    let auth = localStorage.getItem(AUTH.key);
    if (auth) {
        let headers = {};
        headers[token] = auth;
        axios.post(ENGLISH.url + ENGLISH.uri.auth, {}, {
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
    } else {
        gotoLogin();
    }
};

const getwordReciteEchart = function (timeType, successCall=null, errorCall=null) {
    let token = ENGLISH.key;
    let auth = localStorage.getItem(AUTH.key);
    if (auth) {
        let headers = {};
        headers[token] = auth;
        axios.get(ENGLISH.url + ENGLISH.uri.wordReciteEchart, {
            params: {
                time_type: timeType
            },
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
    }
};

const getWordOverview = function (successCall=null, errorCall=null) {
    let token = ENGLISH.key;
    let auth = localStorage.getItem(AUTH.key);
    if (auth) {
        let headers = {};
        headers[token] = auth;
        axios.get(ENGLISH.url + ENGLISH.uri.wordOverview, {
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
    }
};

const getWordDetailReciteHistory = function (categoryId, stack, timeShow, successCall=null, errorCall=null) {
    let token = ENGLISH.key;
    let auth = localStorage.getItem(AUTH.key);
    if (auth) {
        let headers = {};
        headers[token] = auth;
        axios.get(ENGLISH.url + ENGLISH.uri.wordDetailReciteHistory, {
            params: {
                category_id: categoryId,
                stack: stack,
                time: timeShow
            },
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
    }
};

const getWordReciteWord = function (categoryId, wordType, wordNumber, wordRandomMode, successCall=null, errorCall=null) {
    let token = ENGLISH.key;
    let auth = localStorage.getItem(AUTH.key);
    if (auth) {
        let headers = {};
        headers[token] = auth;
        axios.post(ENGLISH.url + ENGLISH.uri.wordReciteWord, {
            category_id: categoryId,
            word_type: wordType,
            word_number: wordNumber,
            word_random_mode: wordRandomMode
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
    }
};

const getWordReciteHistoryWord = function (categoryId, wordType, historyTime, successCall=null, errorCall=null) {
    let token = ENGLISH.key;
    let auth = localStorage.getItem(AUTH.key);
    if (auth) {
        let headers = {};
        headers[token] = auth;
        axios.post(ENGLISH.url + ENGLISH.uri.wordReciteHistoryWord, {
            category_id: categoryId,
            word_type: wordType,
            history_time: historyTime
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
    }
};

const getWordAudio = function (wordId, successCall=null, errorCall=null) {
    let token = ENGLISH.key;
    let auth = localStorage.getItem(AUTH.key);
    if (auth) {
        let headers = {};
        headers[token] = auth;
        axios.post(ENGLISH.url + ENGLISH.uri.wordAudio, {
            word_id: wordId
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
    }
};

const getWordExampleSentence = function (wordId, successCall=null, errorCall=null) {
    let token = ENGLISH.key;
    let auth = localStorage.getItem(AUTH.key);
    if (auth) {
        let headers = {};
        headers[token] = auth;
        axios.get(ENGLISH.url + ENGLISH.uri.wordExampleSentence, {
            params: {
                word_id: wordId
            },
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
    }
};

const getWordExampleSentenceAudio = function (exampleSentenceId, successCall=null, errorCall=null) {
    let token = ENGLISH.key;
    let auth = localStorage.getItem(AUTH.key);
    if (auth) {
        let headers = {};
        headers[token] = auth;
        axios.post(ENGLISH.url + ENGLISH.uri.wordExampleSentenceAudio, {
            example_sentence_id: exampleSentenceId
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
    }
};

const addWordHistory = function (record, successCall=null, errorCall=null) {
    let token = ENGLISH.key;
    let auth = localStorage.getItem(AUTH.key);
    if (auth) {
        let headers = {};
        headers[token] = auth;
        axios.post(ENGLISH.url + ENGLISH.uri.wordAddHistory, {
            record: record
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
    }
};


export {
    authVerify,
    getwordReciteEchart,
    getWordOverview,
    getWordDetailReciteHistory,
    getWordReciteWord,
    getWordReciteHistoryWord,
    getWordAudio,
    getWordExampleSentence,
    getWordExampleSentenceAudio,
    addWordHistory
};
