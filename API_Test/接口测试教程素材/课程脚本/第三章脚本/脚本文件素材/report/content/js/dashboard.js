/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 100.0, "KoPercent": 0.0};
    var dataset = [
        {
            "label" : "KO",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "OK",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.6538461538461539, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [1.0, 500, 1500, "http-post-zxw2018"], "isController": false}, {"data": [0.5, 500, 1500, "HTTP请求"], "isController": false}, {"data": [0.5, 500, 1500, "digest-auth"], "isController": false}, {"data": [0.5, 500, 1500, "C003_V0.9.2_GET Request zxw2018"], "isController": false}, {"data": [0.5, 500, 1500, "http-get"], "isController": false}, {"data": [0.5, 500, 1500, "set-cookie"], "isController": false}, {"data": [0.5, 500, 1500, "C001_V0.9.2_GET Request 51zxw"], "isController": false}, {"data": [0.5, 500, 1500, "get-cookie"], "isController": false}, {"data": [0.5, 500, 1500, "C004_V0.9.2_POST Request zxw666"], "isController": false}, {"data": [1.0, 500, 1500, "get-num"], "isController": false}, {"data": [1.0, 500, 1500, "C002_V0.9.2_POST Request 51zxw"], "isController": false}, {"data": [0.5, 500, 1500, "beanshell_test"], "isController": false}, {"data": [1.0, 500, 1500, "basic-auth"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 13, 0, 0.0, 799.7692307692307, 328, 1421, 1313.0, 1421.0, 1421.0, 1.9055995309293463, 2.3964574629873936, 0.38235098761360303], "isController": false}, "titles": ["Label", "#Samples", "KO", "Error %", "Average", "Min", "Max", "90th pct", "95th pct", "99th pct", "Throughput", "Received", "Sent"], "items": [{"data": ["http-post-zxw2018", 1, 0, 0.0, 440.0, 440, 440, 440.0, 440.0, 440.0, 2.2727272727272725, 1.4515269886363635, 0.48384232954545453], "isController": false}, {"data": ["HTTP请求", 1, 0, 0.0, 1130.0, 1130, 1130, 1130.0, 1130.0, 1130.0, 0.8849557522123894, 0.45112002212389385, 0.127039546460177], "isController": false}, {"data": ["digest-auth", 1, 0, 0.0, 1036.0, 1036, 1036, 1036.0, 1036.0, 1036.0, 0.9652509652509653, 0.31295246138996136, 0.45434664575289574], "isController": false}, {"data": ["C003_V0.9.2_GET Request zxw2018", 1, 0, 0.0, 876.0, 876, 876, 876.0, 876.0, 876.0, 1.141552511415525, 0.5596282819634704, 0.1449236586757991], "isController": false}, {"data": ["http-get", 1, 0, 0.0, 945.0, 945, 945, 945.0, 945.0, 945.0, 1.0582010582010584, 0.6231398809523809, 0.18291170634920637], "isController": false}, {"data": ["set-cookie", 1, 0, 0.0, 637.0, 637, 637, 637.0, 637.0, 637.0, 1.5698587127158556, 1.295440051020408, 0.48291552197802196], "isController": false}, {"data": ["C001_V0.9.2_GET Request 51zxw", 1, 0, 0.0, 1151.0, 1151, 1151, 1151.0, 1151.0, 1151.0, 0.8688097306689835, 0.42252660729800173, 0.10860121633362294], "isController": false}, {"data": ["get-cookie", 1, 0, 0.0, 789.0, 789, 789, 789.0, 789.0, 789.0, 1.2674271229404308, 0.38740692332065907, 0.19308460076045628], "isController": false}, {"data": ["C004_V0.9.2_POST Request zxw666", 1, 0, 0.0, 1421.0, 1421, 1421, 1421.0, 1421.0, 1421.0, 0.7037297677691766, 0.4398311048557354, 0.13675998416608023], "isController": false}, {"data": ["get-num", 1, 0, 0.0, 368.0, 368, 368, 368.0, 368.0, 368.0, 2.717391304347826, 1.3852326766304348, 0.39009425951086957], "isController": false}, {"data": ["C002_V0.9.2_POST Request 51zxw", 1, 0, 0.0, 373.0, 373, 373, 373.0, 373.0, 373.0, 2.680965147453083, 1.6729850871313674, 0.518389745308311], "isController": false}, {"data": ["beanshell_test", 1, 0, 0.0, 903.0, 903, 903, 903.0, 903.0, 903.0, 1.1074197120708749, 11.223439230343299, 0.17844165282392027], "isController": false}, {"data": ["basic-auth", 1, 0, 0.0, 328.0, 328, 328, 328.0, 328.0, 328.0, 3.048780487804878, 0.8723561356707317, 0.6222608612804877], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Percentile 1
            case 8:
            // Percentile 2
            case 9:
            // Percentile 3
            case 10:
            // Throughput
            case 11:
            // Kbytes/s
            case 12:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": []}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 13, 0, null, null, null, null, null, null, null, null, null, null], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
