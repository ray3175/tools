const AUTH = {
    website: "http://ray3175.cn:3399/web/platform/login/index.html",
    name: "用户认证",
    describe: "用户认证接口！",
    url: "http://ray3175.cn:3399",
    uri: {
        authAccount: "/iam/auth/account",       // 登录接口，获取 xy-auth
        auth: "/iam/auth",                      // 通过 xy-auth 获取用户信息
        authLogin: "/iam/auth/login",           // 通过 redirect 方式让 iam 记录用户信息
        login: "/iam/login",                    // 全平台激活 xy-auth
        logout: "/iam/logout",                  // 全平台注销接口
        user: "/iam/user"                       // 注册和修改账号接口
    },
    key: "xy-auth",
    projectName: "tools",
    projectAuthCode: "*t-o-o-l-s*"
};


export { AUTH };
