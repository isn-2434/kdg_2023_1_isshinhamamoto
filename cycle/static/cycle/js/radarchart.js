function radar(item,ctx){
    /* idが"radar-chart"の要素を取得 */
    // var ctx = document.getElementById("radar-chart");
    /* 上記要素にチャートを描画　*/
    var myRadarChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ['値段', '重さ', 'ギア', 'ブレーキ', 'フレーム'],
            datasets: [{
                data: ["{{item.price_rate}}","{{item.weight_rate}}","{{item.gire_rate}}","{{item.brake_rate}}","{{item.frame_rate}}"]
            }]},
        options : {
            animation: { duration: 2000 },
            legend: { display: false },
            scale: {
            ticks: {
                min: 0,
                max: 5,
                stepSize: 1,
                backdropColor: 'rgba(255, 255, 255, 0)',
            }}}
    })
}