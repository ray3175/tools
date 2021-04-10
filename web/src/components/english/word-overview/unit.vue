<template>
    <div class="unit" @click="gotoWordDetail(unitObj)">
        <div class="title">{{ unitObj.name }}</div>
        <div class="info">
            <div>{{ unitObj.recitNumber }}</div>
            <div class="split">/</div>
            <div>{{ unitObj.allNumber }}</div>
        </div>
        <div class="day">
            已背诵
            <span class="day-number">{{ unitObj.recitDay }}</span>
            天
        </div>
    </div>
</template>

<script>
    export default {
        name: "unit",
        props: {
            unitObj: {
                type: Object
            }
        },
        methods: {
            gotoWordDetail(unitObj) {
                this.$router.push({
                    name: "english word-detail",
                    params: {
                        id: unitObj.id,
                        name: unitObj.name
                    }
                });
            }
        }
    }
</script>

<style scoped>
    .unit {
        text-align: center;
        border: 2px solid burlywood;
        border-radius: 5px;
        padding: 5px 10px 5px 10px;
        line-height: 180%;
    }

    .title {
        font-weight: bolder;
        font-size: larger;
    }

    .info {
        font-weight: 600;
        display: flex;
        flex: 1;
        justify-content: center;
    }

    .split {
        margin: 0 10px 0 10px;
    }

    .day {
        font-weight: 600;
    }

    .day-number {
        font-weight: 800;
        color: burlywood;
    }
</style>
