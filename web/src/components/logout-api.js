import { AUTH } from "@/config/auth";


const logoutClick = () => {
    localStorage.removeItem(AUTH.key);
};


export { logoutClick };
