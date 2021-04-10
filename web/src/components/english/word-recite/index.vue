<template>
    <div>
        <div @dblclick="initParams" class="row self-word-recite-title">{{ wordIndex + 1 }} / {{ all }}</div>
        <div class="row self-word-recite">
            <div class="col-6">
                <div v-show="imgAreaShow" id="word-img" class="row self-word-recite-unit">
                    <div class="self-word-recite-border">
                        <img-area :imgBase64="word.img"></img-area>
                    </div>
                </div>
                <div id="word-characters" class="row self-word-recite-unit">
                    <div class="self-word-recite-border">
                        <characters-area
                            ref="charactersArea"
                            :id="word.id"
                            :english="word.english"
                            :chinese="word.chinese"
                            :phoneticSymbol="word.phoneticSymbol"
                        ></characters-area>
                    </div>
                </div>
            </div>
            <div class="col-6">
                <div v-show="exampleSentenceShow" id="word-example-sentence" class="self-word-recite-unit">
                    <div id="word-example-sentence-main" class="self-word-recite-border">
                        <example-sentence ref="exampleSentence"></example-sentence>
                    </div>
                </div>
                <div id="word-recite-input" class="self-word-recite-unit">
                    <div class="self-word-recite-border">
                        <verify-area ref="verifyArea"></verify-area>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { getDateString } from "@/utils/time";
    import { getWordReciteWord, getWordReciteHistoryWord, addWordHistory } from "@/api/english";

    import verifyArea from "./verify-area";
    import charactersArea from "./characters-area";
    import imgArea from "./img-area";
    import exampleSentence from "./example-sentence";

    export default {
        name: "word-recite",
        components: {
            "verify-area": verifyArea,
            "characters-area": charactersArea,
            "img-area": imgArea,
            "example-sentence": exampleSentence
        },
        data() {
            return {
                imgAreaShow: true,
                exampleSentenceShow: true,

                autoPlayAudio: false,

                wordList: [],
                wordIndex: 0,
                all: 0,

                audioElement: null,

                record: [],
                tmpConsoleRecord: {},

                isOver: false,
                isPushToBackService: false
            };
        },
        mounted() {
            let id = this.$route.params.id || this.$route.query.id;
            let wordType = this.$route.params.wordType || this.$route.query.wordType;
            let wordNumber = Number(this.$route.params.wordNumber);
            let wordRandomMode = this.$route.params.wordRandomMode;
            let historyTime = this.$route.query.historyTime;
            if (id) {
                if (historyTime) {
                    getWordReciteHistoryWord(id, wordType, historyTime, (rsp) => {
                        if (rsp.data.code === 200) {
                            this.wordList = rsp.data.data;
                            this.all = this.wordList.length;
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                } else {
                    getWordReciteWord(id, wordType, wordNumber, wordRandomMode, (rsp) => {
                        if (rsp.data.code === 200) {
                            this.wordList = rsp.data.data;
                            this.all = Math.min(this.wordList.length, wordNumber);
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                }
            } else {
                this.$router.push({
                    path: "/english"
                });
            }
        },
        computed: {
            word() {
                let wordNow = this.wordList[this.wordIndex];
                return wordNow ? {
                    id: wordNow.id,
                    english: wordNow.english,
                    chinese: wordNow.chinese,
                    phoneticSymbol: wordNow.phonetic_symbol,
                    img: wordNow.img
                } : {}
            }
        },
        methods: {
            initParams() {
                this.imgAreaShow = true;
                this.exampleSentenceShow = true;
            },
            playAudio(content) {
                let audio = document.createElement("audio");
                if (audio !== null && audio.canPlayType && audio.canPlayType("audio/mpeg")) {
                    if (this.audioElement) {
                        this.audioElement.pause();
                    }
                    audio.src = "data:audio/mpeg;base64," + content;
                    this.audioElement = audio;
                    audio.play();
                }
            },
            verifyWord(text) {
                let isSuccess = text ? this.word.chinese.includes(text) : false;
                let wordId = this.word.id;
                this.tmpConsoleRecord = {
                    category_id: this.$route.params.id || this.$route.query.id,
                    word_id: wordId,
                    time: getDateString(),
                    error: !isSuccess
                };
                this.$refs.exampleSentence.getExampleSentenceList(wordId);
                this.$refs.verifyArea.resultStatus(isSuccess);
                this.$refs.charactersArea.alterChineseShow(true);
            },
            erroneousJudgement() {
                this.tmpConsoleRecord.error = false;
            },
            nextWord() {
                if (!this.isOver) {
                    this.record.push(this.tmpConsoleRecord);
                }
                if (this.wordIndex+1 < this.all) {
                    this.wordIndex++;
                    this.$refs.exampleSentence.initExampleSentence();
                    this.$refs.verifyArea.initVerifyArea();
                    this.$refs.charactersArea.initCharactersArea();
                } else {
                    this.isOver = true;
                    if (!this.isPushToBackService) {
                        this.isPushToBackService = true;
                        addWordHistory(this.record, (rsp) => {
                            alert(rsp.data.msg);
                            if (rsp.data.code === 200) {
                                this.$router.push({
                                    name: "english word-detail",
                                    params: {
                                        id: this.$route.params.id || this.$route.query.id,
                                        name: this.$route.params.name
                                    }
                                });
                            } else {
                                this.isPushToBackService = false;
                            }
                        })
                    } else {
                        alert("正在将背诵结果传给后台，请勿重复提交！");
                    }
                }
            }
        }
    }
</script>

<style scoped>
    .self-word-recite-title {
        font-size: 500%;
        font-weight: bolder;
        font-style: italic;
        color: burlywood;
        display: flex;
        justify-content: center;
    }

    .self-word-recite {
        margin-top: 10px;
    }

    @media (max-width: 800px) {
        .self-word-recite {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
    }

    .self-word-recite-unit {
        padding: 5px 10px 5px 10px;
    }

    .self-word-recite-border {
        width: 100%;
        height: 100%;
        border: 2px solid burlywood;
        border-radius: 5px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    #word-img {
        height: 400px;
    }

    #word-characters {
        height: 200px;
    }

    #word-example-sentence {
        height: 450px;
    }

    #word-example-sentence-main {
        overflow: scroll;
        flex-direction: column;
        align-items: flex-start !important;
    }

    /* 滚动条消失 */
    #word-example-sentence-main::-webkit-scrollbar {
        width: 4px;
        height: 4px;
    }

    /* 滚动条颜色 */
    #word-example-sentence-main::-webkit-scrollbar-thumb {
        border-radius: 5px;
        -webkit-box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
        background: rgba(0,0,0,0.2);
    }

    /* 滚动条轨道 */
    #word-example-sentence-main::-webkit-scrollbar-track {
        -webkit-box-shadow: inset 0 0 5px rgba(0,0,0,0);
        border-radius: 0;
        background: rgba(0,0,0,0);
    }

    #word-recite-input {
        height: 150px;
    }
</style>
