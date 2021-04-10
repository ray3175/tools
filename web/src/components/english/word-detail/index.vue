<template>
    <div class="english-word-detail">
        <div class="row self-title-row">
            <div class="title">{{ title }}</div>
        </div>
        <div class="row english-word-info">
            <div class="col-md-4">
                <recite-setting></recite-setting>
            </div>
            <div class="col-md-8">
                <recite-history ref="reciteHistory" :value="value" :categoryId="id"></recite-history>
            </div>
        </div>
    </div>
</template>

<script>
    import { getWordDetailReciteHistory } from "@/api/english";

    import reciteSetting from "./recite-setting";
    import reciteHistory from "./recite-history";

    export default {
        name: "word-detail",
        components: {
            "recite-setting": reciteSetting,
            "recite-history": reciteHistory
        },
        data() {
            return {
                id: this.$route.params.id,
                title: this.$route.params.name,
                value: []
            };
        },
        mounted() {
            if (this.id) {
                getWordDetailReciteHistory(this.id, 0, null, (rsp) => {
                    if (rsp.data.code === 200) {
                        this.value = this.$refs.reciteHistory.initValue(rsp.data.data);
                    } else {
                        alert(rsp.data.msg);
                    }
                });
            } else {
                this.$router.push({
                    path: "/english"
                });
            }
        }
    }
</script>

<style scoped>
    .self-title-row {
        font-size: 500%;
        font-weight: bolder;
        font-style: italic;
        color: burlywood;
        display: flex;
        justify-content: center;
        margin: 10px 0 20px 0;
    }

    .english-word-info {
        border: 2px solid burlywood;
        border-radius: 5px;
        padding: 5px 0 10px 0;
    }
</style>
