<template>
    <div id="self-echart-word-recite" ref="englishEchart"></div>
</template>

<script>
    import { getwordReciteEchart } from "@/api/english";

    export default {
        name: "word-recite-echart",
        props: ["timeType"],
        mounted () {
            this.getEchartData(this.timeType);
        },
        watch: {
            timeType(value) {
                this.getEchartData(value);
            }
        },
        methods: {
            initEcharts (time, seriesAll, seriesSuccess, seriesError, seriesErrorRepeat, seriesErrorRepeatIn30Day, seriesErrorRepeatIn7Day) {
                let eChart = this.$echarts.init(this.$refs.englishEchart);
                eChart.setOption({
                    title: {
                        text: "单词背诵"
                    },
                    tooltip: {
                        trigger: "axis"
                    },
                    legend: {
                        data: ["总数", "正确数", "错误数", "重复错误数", "30天重复错误数", "7天重复错误数"]
                    },
                    grid: {
                        left: "3%",
                        right: "4%",
                        bottom: "3%",
                        containLabel: true
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        type: "category",
                        boundaryGap: false,
                        data: time
                    },
                    yAxis: {
                        type: "value"
                    },
                    series: [
                        {
                            name: "总数",
                            type: "line",
                            smooth: true,
                            data: seriesAll
                        },
                        {
                            name: "正确数",
                            type: "line",
                            smooth: true,
                            data: seriesSuccess
                        },
                        {
                            name: "错误数",
                            type: "line",
                            smooth: true,
                            data: seriesError
                        },
                        {
                            name: "重复错误数",
                            type: "line",
                            smooth: true,
                            data: seriesErrorRepeat
                        },
                        {
                            name: "30天重复错误数",
                            type: "line",
                            smooth: true,
                            data: seriesErrorRepeatIn30Day
                        },
                        {
                            name: "7天重复错误数",
                            type: "line",
                            smooth: true,
                            data: seriesErrorRepeatIn7Day
                        }
                    ]
                }, true);
            },
            initDataAndEchart(data) {
                let time = [];
                let seriesAll = [];
                let seriesSuccess = [];
                let seriesError = [];
                let seriesErrorRepeat = [];
                let seriesErrorRepeatIn30Day = [];
                let seriesErrorRepeatIn7Day = [];
                for (let i in data) {
                    time.push(data[i].date);
                    seriesAll.push(data[i].all);
                    seriesSuccess.push(data[i].all - data[i].error);
                    seriesError.push(data[i].error);
                    seriesErrorRepeat.push(data[i].error_repeat);
                    seriesErrorRepeatIn30Day.push(data[i].error_repeat_in_30_day);
                    seriesErrorRepeatIn7Day.push(data[i].error_repeat_in_7_day);
                }
                this.initEcharts(time, seriesAll, seriesSuccess, seriesError, seriesErrorRepeat, seriesErrorRepeatIn30Day, seriesErrorRepeatIn7Day);
            },
            getEchartData(timeType) {
                getwordReciteEchart(timeType, (rsp) => {
                    if(rsp.data.code === 200) {
                        this.initDataAndEchart(rsp.data.data);
                    } else {
                        alert(rsp.data.msg);
                    }
                });
            }
        }
    }
</script>

<style scoped>
    #self-echart-word-recite {
        width: 1110px;
        height: 500px;
    }
</style>
