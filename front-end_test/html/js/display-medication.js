const queryParams = new URLSearchParams(window.location.search);
const patientName = queryParams.get('patientName');
const visitDate = queryParams.get('visitDate');
const medications = JSON.parse(queryParams.get('medications'));

document.getElementById('patient-name').textContent = patientName;
document.getElementById('visit-date').textContent = visitDate;

const medicationsContainer = document.getElementById('medications');

medications.forEach(medication => {
    const medicationItem = document.createElement('div');
    medicationItem.classList.add('medication-item');

    const medicationName = document.createElement('p');
    medicationName.textContent = `약물 이름: ${medication.name}`;
    medicationItem.appendChild(medicationName);

    const medicationDose = document.createElement('p');
    medicationDose.textContent = `복용량: ${medication.dose}`;
    medicationItem.appendChild(medicationDose);

    const medicationTimes = document.createElement('p');
    medicationTimes.textContent = `복용 시간: ${medication.times}`;
    medicationItem.appendChild(medicationTimes);

    medicationsContainer.appendChild(medicationItem);
});



function addMedication() {
    window.location.href = './add-medication.html';
  }
  
  function navigateBack() {
    window.location.href = './main.html';
  }
  