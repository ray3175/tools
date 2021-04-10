<template>
    <div class="english-word-overview">
        <div v-for="unitList in unitRow" class="row unit">
            <div v-for="unitObj in unitList" class="col-3 cursor-pointer">
                <unit :unitObj="unitObj"></unit>
            </div>
        </div>
    </div>
</template>

<script>
    import { getWordOverview } from "@/api/english";

    import unit from "./unit";

    export default {
        name: "word-overview",
        components: { unit },
        data() {
            return {
                unitRow: []
            };
        },
        mounted() {
            getWordOverview((rsp) => {
                if (rsp.data.code === 200) {
                    this.unitRow = this.newUnitRow(rsp.data.data);
                } else {
                    alert(rsp.data.msg);
                }
            });
        },
        methods: {
            newUnitRow(unitList) {
                let unitRow = [];
                let x = 0;
                let tmpList = [];
                for (let i in unitList) {
                    unitList[i].allNumber = unitList[i].all_number;
                    unitList[i].recitDay = unitList[i].recit_day;
                    unitList[i].recitNumber = unitList[i].recit_number;
                    x++;
                    tmpList.push(unitList[i]);
                    if (x >= 4) {
                        unitRow.push(tmpList);
                        tmpList = [];
                        x = 0;
                    }
                }
                if (tmpList.length) {
                    unitRow.push(tmpList);
                }
                return unitRow;
            }
        }
    }
</script>

<style scoped>
    .unit {
        margin-top: 15px;
    }

    .cursor-pointer {
        cursor: pointer;
    }
</style>
