import root from '@/components/english/root';
import wordOverview from '@/components/english/word-overview';
import wordDetail from '@/components/english/word-detail';
import wordRecite from '@/components/english/word-recite';


const englishChildren = [
    {
        path: "",
        redirect: "root"
    },
    {
        path: "root",
        name: "english root",
        component: root
    },
    {
        path: "word-overview",
        name: "english word-overview",
        component: wordOverview
    },
    {
        path: "word-detail",
        name: "english word-detail",
        component: wordDetail
    },
    {
        path: "word-recite",
        name: "english word-recite",
        component: wordRecite
    }
];


export { englishChildren };
