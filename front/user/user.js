import apiClient from "../apiClient.js";

document.addEventListener('DOMContentLoaded', () => {
    function getThresholdValues() {
        const yellowThresholdInput = document.getElementById('yellow-threshold');
        const redThresholdInput = document.getElementById('red-threshold');

        const yellowThreshold = yellowThresholdInput ? parseFloat(yellowThresholdInput.value) || 0.6 : 0.6;
        const redThreshold = redThresholdInput ? parseFloat(redThresholdInput.value) || 0.8 : 0.8;
        return { yellowThreshold, redThreshold };
    }

    function getCellStyle(coefficient) {
        const { yellowThreshold, redThreshold } = getThresholdValues();

        let color = '';
        let opacity = 0.5;

        if (coefficient >= redThreshold) {
            opacity += 0.5 * (coefficient - redThreshold) / (1 - redThreshold);
            color = `rgba(255, 0, 0, ${opacity})`;
        } else if (coefficient >= yellowThreshold) {
            opacity += 0.5 * (coefficient - yellowThreshold) / (redThreshold - yellowThreshold);
            color = `rgba(255, 255, 0, ${opacity})`;
        } else {
            opacity += 0.5 * coefficient / yellowThreshold;
            color = `rgba(0, 255, 0, ${opacity})`;
        }

        return `background-color: ${color};`;
    }

    function fetchUserData() {
        const userName = new URLSearchParams(window.location.search).get('name');
        apiClient.get(`/get/user/${userName}`)
            .then(response => {
                const userData = response.data;

                const users = userData.table;

                const userHeader = document.getElementById('user-header');
                userHeader.textContent = `Название файла: ${userData.name}`;

                const homeworkIds = users[0].coefficients.map(item => item.homework_id);

                const thead = document.querySelector('#coefficients-table thead tr');
                thead.innerHTML = '<th>ID задания / ID студента</th>';
                homeworkIds.forEach(id => {
                    const th = document.createElement('th');
                    th.textContent = `ДЗ ${id}`;
                    thead.appendChild(th);
                });

                const tbody = document.querySelector('#coefficients-table-body');
                tbody.innerHTML = '';

                users.forEach(user => {
                    const row = document.createElement('tr');

                    const idCell = document.createElement('td');
                    const link = document.createElement('a');
                    link.href = `http://127.0.0.1:8080/user/?name=${user.name}`;
                    link.textContent = user.name;
                    link.classList.add('user-link-cell');
                    idCell.appendChild(link);
                    row.appendChild(idCell);

                    const userCoefficients = user.coefficients.map(item => item.coefficient);
                    homeworkIds.forEach(id => {
                        const td = document.createElement('td');
                        const coefficient = user.coefficients.find((item) => item.homework_id === id)?.coefficient || '-';

                        if (typeof coefficient === 'number') {
                            td.style = getCellStyle(coefficient);
                        }

                        td.textContent = coefficient !== '-' ? coefficient.toFixed(2) : '-';
                        row.appendChild(td);
                    });

                    tbody.appendChild(row);
                });
            })
            .catch(error => {
                console.error('Error fetching user data:', error);
            });
    }

    const yellowThresholdInput = document.getElementById('yellow-threshold');
    const redThresholdInput = document.getElementById('red-threshold');
    if (yellowThresholdInput && redThresholdInput) {
        yellowThresholdInput.addEventListener('input', fetchUserData);
        redThresholdInput.addEventListener('input', fetchUserData);
    }

    fetchUserData();
});