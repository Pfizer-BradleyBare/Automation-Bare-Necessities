function filter_log_level() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("input-log-level");
    filter = input.value.toUpperCase();
    table = document.getElementById("trace-table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1 || filter === "ALL") {
            tr[i].filter_log_level = false
        } else {
            tr[i].filter_log_level = true
        }
        }
    }
    filter_final()
}

function filter_method_name() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("input-method-name");
    filter = input.value.toUpperCase();
    table = document.getElementById("trace-table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[2];
        if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].filter_method_name = false
        } else {
            tr[i].filter_method_name = true
        }
        }
    }
    filter_final()
}

function filter_device_identifier() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("input-device-identifier");
    filter = input.value.toUpperCase();
    table = document.getElementById("trace-table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[3];
        if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].filter_device_identifier = false
        } else {
            tr[i].filter_device_identifier = true
        }
        }
    }
    filter_final()
}

function filter_debug_message() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("input-debug-message");
    filter = input.value.toUpperCase();
    table = document.getElementById("trace-table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[4];
        if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].filter_debug_message = false
        } else {
            tr[i].filter_debug_message = true
        }
        }
    }
    filter_final()
}

function filter_final() {
    var table, tr, i,filter_debug_message,filter_device_identifier,filter_log_level,filter_method_name;
    table = document.getElementById("trace-table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        filter_debug_message = !!tr[i].filter_debug_message
        filter_device_identifier = !!tr[i].filter_device_identifier
        filter_log_level = !!tr[i].filter_log_level
        filter_method_name = !!tr[i].filter_method_name

        if (filter_debug_message === false && filter_device_identifier === false && filter_log_level === false && filter_method_name === false ) {
            tr[i].style.display = ""
        } else {
            tr[i].style.display = "none"
        }
    }
}