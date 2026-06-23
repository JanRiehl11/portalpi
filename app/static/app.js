const bootScreen = document.getElementById('boot-screen');
const homeScreen = document.getElementById('home-screen');
const toast = document.getElementById('toast');
const quickSettingsPanel = document.getElementById('quick-settings-panel');

function showToast(message) {
  toast.textContent = message;
  toast.classList.add('visible');
  setTimeout(() => toast.classList.remove('visible'), 2400);
}

async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });

  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.message || 'Request failed');
  }
  return data;
}

function setText(id, value) {
  const node = document.getElementById(id);
  if (node) node.textContent = value;
}

async function loadStatus() {
  try {
    const status = await api('/api/status');
    setText('wifi-status', status.wifi || 'Offline');
    setText('ip-status', status.ip_address || '—');
    setText('temp-status', status.cpu_temp_c ? `${status.cpu_temp_c}°C` : '—');
    setText('device-name', status.device_name || '—');
    setText('platform-name', status.platform || '—');
    setText('chiaki-status', status.chiaki_installed ? 'Installed' : 'Not installed');
    setText('disk-status', `${status.disk.free_gb} GB free`);
    setText('qs-wifi', status.wifi || 'Offline');
    setText('qs-ip', status.ip_address || '—');
    setText('qs-temp', status.cpu_temp_c ? `${status.cpu_temp_c}°C` : '—');
    setText('qs-version', status.portalpi_version || '—');
  } catch (error) {
    showToast(error.message);
  }
}

async function launchChiaki() {
  try {
    const result = await api('/api/launch/chiaki', { method: 'POST' });
    showToast(result.message || 'Chiaki launched');
  } catch (error) {
    showToast(error.message);
  }
}

async function powerAction(path, label) {
  try {
    const result = await api(path, { method: 'POST' });
    showToast(result.message || label);
  } catch (error) {
    showToast(error.message);
  }
}

function openQuickSettings() {
  quickSettingsPanel.classList.remove('hidden');
}

function closeQuickSettings() {
  quickSettingsPanel.classList.add('hidden');
}

function init() {
  setTimeout(() => {
    bootScreen.classList.remove('active');
    homeScreen.classList.add('active');
    loadStatus();
  }, 1700);

  document.getElementById('launch-chiaki').addEventListener('click', launchChiaki);
  document.getElementById('refresh-status').addEventListener('click', loadStatus);
  document.getElementById('quick-settings-button').addEventListener('click', openQuickSettings);
  document.getElementById('close-settings').addEventListener('click', closeQuickSettings);
  document.getElementById('reboot-button').addEventListener('click', () => powerAction('/api/power/reboot', 'Rebooting'));
  document.getElementById('shutdown-button').addEventListener('click', () => powerAction('/api/power/shutdown', 'Shutting down'));

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeQuickSettings();
    if (event.key.toLowerCase() === 'q') openQuickSettings();
  });
}

init();
