import root from '@/components/verification-code/root';
import shortMessage from '@/components/verification-code/short-message';
import history from '@/components/verification-code/history';


const verificationCodeChildren = [
    {
        path: "",
        redirect: "root"
    },
    {
        path: "root",
        name: "verification-code root",
        component: root
    },
    {
        path: "short-message",
        name: "verification-code short-message",
        component: shortMessage
    },
    {
        path: "history",
        name: "verification-code history",
        component: history
    }
];


export { verificationCodeChildren };
