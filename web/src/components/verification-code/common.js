function getPlatformListFromLocalStorage() {
    let platformListString = localStorage.getItem("verification-code");
    return platformListString ? JSON.parse(platformListString) : [];
}

function getPlatform(name) {
    let platformList = getPlatformListFromLocalStorage();
    let platform = {};
    platformList.forEach((value) => {
        if (value.name === name) {
            platform = value;
        }
    });
    return platform;
}

function setPlatformListToLocalStorage(platformList) {
    localStorage.setItem("verification-code", JSON.stringify(platformList));
}

function setPlatformUserPassword(name, user, password) {
    let platformList = getPlatformListFromLocalStorage();
    let needPush = true;
    if (platformList.length) {
        platformList.forEach((value) => {
            if (needPush && value.name === name) {
                value.user = user;
                value.password = password;
                needPush = false;
            }
        });
    }
    if (needPush) {
        platformList.push({
            name: name,
            user: user,
            password: password
        });
    }
    setPlatformListToLocalStorage(platformList);
}



export { getPlatformListFromLocalStorage, getPlatform, setPlatformUserPassword };
