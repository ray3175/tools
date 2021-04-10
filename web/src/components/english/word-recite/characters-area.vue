<template>
    <div class="characters-area">
        <div @click="getAudio" :class="audioLoading ? 'audio-loading' : 'audio-normal'" class="characters-area-text">{{ english }}&nbsp;&nbsp;&nbsp;&nbsp;{{ phoneticSymbol }}</div>
        <div v-show="chineseShow" class="characters-area-text">{{ chinese }}</div>
    </div>
</template>

<script>
    import { getWordAudio } from "@/api/english";

    export default {
        name: "characters-area",
        props: ["id", "english", "chinese", "phoneticSymbol"],
        data() {
            return {
                audioLoading: false,
                chineseShow: false
            };
        },
        watch: {
            id() {
                if (this.$parent.autoPlayAudio) {
                    setTimeout(() => {
                        this.getAudio();
                    }, 100);
                }
            }
        },
        methods: {
            initCharactersArea() {
                this.alterChineseShow(false);
            },
            getAudio() {
                this.audioLoading = true;
                getWordAudio(this.id, (rsp) => {
                    if (rsp.data !== 0) {
                        this.audioLoading = false;
                        this.$parent.playAudio(rsp.data);
                    } else {
                        alert("该词汇暂无音频数据！");
                    }
                });
            },
            alterChineseShow(status) {
                this.chineseShow = status;
            }
        }
    }
</script>

<style scoped>
    .characters-area {
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }

    .characters-area-text {
        font-size: 150%;
        font-weight: bolder;
    }

    .audio-normal {
        cursor: pointer;
    }

    .audio-loading {
        cursor: wait;
    }
</style>
