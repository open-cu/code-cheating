import apiClient from './apiClient';

function getThresholdValues() {
    const yellowThreshold = parseFloat(document.getElementById('yellow-threshold').value) || 0.3;
    const redThreshold = parseFloat(document.getElementById('red-threshold').value) || 0.5;
    return { yellowThreshold, redThreshold };
}

function getCellClass(value) {
    const { yellowThreshold, redThreshold } = getThresholdValues();

    if (value > redThreshold) {
        return 'red-row';
    } else if (value > yellowThreshold) {
        return 'yellow-row';
    } else {
        return 'green-row';
    }
}

function createTableRow(user) {
    return `
        <tr data-name="${user.name}">
            <td>${user.name}</td>
            <td>${user.level}</td>
            <td class="${getCellClass(user.average_coefficient)}">${user.average_coefficient.toFixed(4)}</td>
            <td class="${getCellClass(user.maximum_coefficient)}">${user.maximum_coefficient.toFixed(4)}</td>
            <td class="${getCellClass(user.median_coefficient)}">${user.median_coefficient.toFixed(4)}</td>
        </tr>
    `;
}

function updateTable(data) {
    const tableBody = document.getElementById('user-table-body');
    tableBody.innerHTML = data.map(createTableRow).join('');
    addRowClickListeners();
}

function sortData(criterion, users) {
    const sortedUsers = [...users].sort((a, b) => b[criterion] - a[criterion]);
    updateTable(sortedUsers);
}

function addRowClickListeners() {
    const rows = document.querySelectorAll('#user-table-body tr');
    rows.forEach(row => {
        row.addEventListener('click', () => {
            const userName = row.getAttribute('data-name');
            window.location.href = `./user/index.html?name=${userName}`;
        });
    });
}

function setActiveButton(activeId) {
    document.querySelectorAll('.sort-button').forEach(button => {
        button.classList.toggle('active', button.id === activeId);
    });
}

function fetchDataAndInitialize() {
    apiClient.get('/get/all_users')
        .then(response => {
            const users = response.data;

            sortData('average_coefficient', users);
            setActiveButton('sort-average');

            document.getElementById('sort-average').addEventListener('click', () => {
                setActiveButton('sort-average');
                sortData('average_coefficient', users);
            });

            document.getElementById('sort-median').addEventListener('click', () => {
                setActiveButton('sort-median');
                sortData('median_coefficient', users);
            });

            document.getElementById('sort-maximum').addEventListener('click', () => {
                setActiveButton('sort-maximum');
                sortData('maximum_coefficient', users);
            });

            document.getElementById('yellow-threshold').addEventListener('input', () => {
                sortData(document.querySelector('.sort-button.active').id.split('-')[1], users);
            });

            document.getElementById('red-threshold').addEventListener('input', () => {
                sortData(document.querySelector('.sort-button.active').id.split('-')[1], users);
            });
        })
        .catch(error => {
            console.error('Error fetching users:', error);
        });
}

document.addEventListener('DOMContentLoaded', () => {
    fetchDataAndInitialize();
});