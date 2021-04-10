<template>
    <div @dblclick="hide" id="self-example-sentence">
        <div v-for="(obj, index) in exampleSentenceList" class="example-sentence-unit">
            <div @click="getAudio(obj)" :class="audioLoading ? 'audio-loading' : 'audio-normal'" class="example-sentence-english-text">{{ obj.english }}</div>
            <div class="example-sentence-chinese-text">{{ obj.chinese }}</div>
        </div>
    </div>
</template>

<script>
    import { getWordExampleSentence, getWordExampleSentenceAudio } from "@/api/english";

    export default {
        name: 'example-sentence',
        data() {
            return {
                audioLoading: false,
                exampleSentenceList: []
            };
        },
        methods: {
            hide() {
                this.$parent.exampleSentenceShow = false;
            },
            initExampleSentence() {
                this.exampleSentenceList = [];
            },
            getExampleSentenceList(wordId) {
                if (this.$parent.exampleSentenceShow) {
                    getWordExampleSentence(wordId, (rsp) => {
                        if (rsp.data.code === 200) {
                            this.exampleSentenceList = rsp.data.data;
                        } else {
                            alert(rsp.data.msg);
                        }
                    });
                }
            },
            getAudio(obj) {
                this.audioLoading = true;
                getWordExampleSentenceAudio(obj.id, (rsp) => {
                    if (rsp.data !== 0) {
                        this.audioLoading = false;
                        this.$parent.playAudio(rsp.data);
                    } else {
                        alert("该例句暂无音频数据！");
                    }
                });
            }
        }
    }
</script>

<style scoped>
    #self-example-sentence {
        width: 100%;
        height: 100%;
    }

    .example-sentence-unit {
        border: 2px solid burlywood;
        border-radius: 5px;
        padding: 5px 15px 5px 15px;
        margin: 5px 0 5px 5px;
    }

    .example-sentence-english-text {
        font-size: 110%;
        font-weight: bold;
    }

    .example-sentence-chinese-text {
        font-weight: bolder;
    }

    .audio-normal {
        cursor: pointer;
    }

    .audio-loading {
        cursor: wait;
    }
</style>
