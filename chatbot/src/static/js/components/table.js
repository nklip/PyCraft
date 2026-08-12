// global, keeps the order of attributes / keys
let keyOrder = new Object()

function addTable(table, clickable) {
    setTimeout(() => {
        const numberOrRowToDisplay = 5;
        // take all attributes from the first row
        let columns = Object.keys(table[0]);
        const tablePopup = document.getElementById("tablePopupContainer");
        const chatContainer = document.getElementById("chats");
        // exclude next attributes from the output
        let keysToExclude = ['RowIndex', 'AddStr']
        columns = columns.filter(key => !keysToExclude.includes(key));
        // set dictionary
        for (let key = 0; key < columns.length; key++) {
            keyOrder[columns[key].toLowerCase()] = key;
        }
        // add all attributes from the first row as columns
        let mainTable = addColumnsInChat(columns);
        // form table body
        const tableContainer = document.createElement('div');
        tableContainer.classList.add('singleCardNew');
        const numRows = Math.min(numberOrRowToDisplay, table.length);
        for (let row = 0; row < numRows; row++) {
            if (clickable) {
                mainTable += `<tr class="custom-row">`;
            } else {
                mainTable += `<tr>`;
            }
            for (let col = 0; col < columns.length; col++) {
                mainTable += `<td>${table[row][columns[col]]}</td>`;
            }
            mainTable += `</tr>`;
        }
        // only add 'Show More' as a row if there are more than N rows
        if (table.length > numberOrRowToDisplay) {
            mainTable +=
                `<tr id="showMoreRow">` +
                    `<td colspan="3" style="text-align:center">` +
                        `<a class="showMore" style="cursor:pointer">Show More</a>` +
                    `</td>` +
                `</tr>`;
        }
        mainTable += `</tbody></table>`;
        tableContainer.innerHTML = mainTable;
        chatContainer.appendChild(tableContainer);

        scrollToBottomOfResults();

        $(document).on("click", ".exp-table .showMore", function() {
            let fullTable = createTableBody(table, columns, clickable);
            fullTable += `</tbody></table>`;
            tablePopup.innerHTML = fullTable;
            document.querySelector('.popup').style.display = "block";
        });
    }, 1000);
};

function createTableBody(table, columns, clickable) {
    let tab = addColumnsInChat(columns);
    for (let k = 0; k < table.length; k++) {
        if (clickable) {
            tab += `<tr class="custom-row">`;
        } else {
            tab += `<tr>`;
        }
        for (let col = 0; col < columns.length; col++) {
            tab += `<td>${table[k][columns[col]]}</td>`;
        }
        tab += `</tr>`;
    }
    return tab;
};

function addColumnsInChat(columns) {
    const columnsHtmlHeader =
        `<table class="exp-table table-bordered">` +
            `<thead>` +
                `<tr class="headerTitle">`;
    const columnsHtmlFooter =
                `</tr>` +
            '</thead>' +
            '<tbody>';

    let columnsHtml = columnsHtmlHeader;
    for (let i = 0; i < columns.length; i++) {
        columnsHtml += `<th>${columns[i]}</th>`;
    }
    columnsHtml += columnsHtmlFooter;
    return columnsHtml;
};

$(document).on("click", ".exp-table .custom-row", function() {
    const rowData = $(this).childred('td').map(function() {
        return $(this).text();
    });

    const text = rowData[0] + " " + rowData[1];

    document.querySelector('.popup').style.display = "none";

    if (payload["context"]["entities"]["selected_id"] !== undefined) {
        payload["context"]["entities"]["selected_id"] = `${rowData[keyOrder['id']]}`;
    }
    if (payload["context"]["entities"]["selected_type"] !== undefined) {
        payload["context"]["entities"]["selected_type"] = `${rowData[keyOrder['id']]}`;
    }
    if (payload["context"]["entities"]["selected_name"] !== undefined) {
        payload["context"]["entities"]["selected_name"] = `${rowData[keyOrder['type']]}`
    }
    setUserResponse(text);
    sendMessage(payload);
});

$(document).on("click", ".popup .icon", function() {
    document.querySelector('.popup').style.display = "none";
});