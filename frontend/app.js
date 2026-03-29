// Config
// Si tu API corre en otro puerto o IP, cambia esto:
const API_BASE = localStorage.getItem('API_BASE') || 'http://127.0.0.1:8000';

// Utilidad para mostrar en UI
document.getElementById('apiBaseText').textContent = API_BASE;

// Helpers
const $ = (sel) => document.querySelector(sel);

function toast(title, message){
  const area = $('#toastArea');
  const el = document.createElement('div');
  el.className = 'toast';
  el.innerHTML = `<strong>${escapeHtml(title)}</strong><p>${escapeHtml(message)}</p>`;
  area.appendChild(el);
  setTimeout(() => el.remove(), 3800);
}

function escapeHtml(str){
  return String(str)
    .replaceAll('&','&amp;')
    .replaceAll('<','&lt;')
    .replaceAll('>','&gt;')
    .replaceAll('"','&quot;')
    .replaceAll("'",'&#039;');
}

async function api(path, options={}){
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { 'Content-Type': 'application/json', ...(options.headers||{}) },
    ...options
  });

  const text = await res.text();
  let data = null;
  try { data = text ? JSON.parse(text) : null; } catch { data = { raw: text }; }

  if(!res.ok){
    const detail = data?.detail || data?.message || JSON.stringify(data);
    throw new Error(`${res.status} ${res.statusText} - ${detail}`);
  }
  return data;
}

function fillTable(tbodyId, rowsHtml, emptyCols){
  const tbody = document.getElementById(tbodyId);
  if(!rowsHtml.length){
    tbody.innerHTML = `<tr><td colspan="${emptyCols}" class="muted">Sin datos…</td></tr>`;
    return;
  }
  tbody.innerHTML = rowsHtml.join('');
}

// Health
async function loadHealth(){
  const pill = $('#healthPill');
  try{
    const data = await api('/health');
    pill.textContent = `OK • ${data.service}`;
    pill.style.borderColor = 'rgba(0,255,180,.28)';
    pill.style.background = 'rgba(0,255,180,.10)';
    $('#healthMeta').textContent = `timestamp: ${data.timestamp}`;
  }catch(err){
    pill.textContent = 'Sin conexión';
    pill.style.borderColor = 'rgba(255,80,120,.35)';
    pill.style.background = 'rgba(255,80,120,.12)';
    $('#healthMeta').textContent = 'Revisa que la API esté corriendo (uvicorn) y CORS habilitado.';
  }
}

// Users (GET/POST/PUT/DELETE)
let lastUsers = [];

async function loadUsers(){
  try{
    const data = await api('/users/');
    const items = data.items || [];
    lastUsers = items;

    fillTable('usersTbody', items.map(u => (
      `<tr>
        <td>${u.id ?? ''}</td>
        <td>${escapeHtml(u.name ?? '')}</td>
        <td>${escapeHtml(u.role ?? '')}</td>
        <td>${u.active ? 'Sí' : 'No'}</td>
        <td>
          <div class="rowActions">
            <button class="btn ghost" type="button" data-edit="${u.id}">Editar</button>
            <button class="btn danger" type="button" data-del="${u.id}">Eliminar</button>
          </div>
        </td>
      </tr>`
    )), 5);

    // Edit / Delete handlers
    document.querySelectorAll('[data-edit]').forEach(btn => {
      btn.addEventListener('click', () => {
        const id = Number(btn.getAttribute('data-edit'));
        const user = lastUsers.find(x => x.id === id);
        if(!user) return;
        const form = $('#formUser');
        form.user_id.value = user.id;
        form.name.value = user.name;
        form.role.value = user.role;
        form.active.checked = !!user.active;
        toast('Editar', `Usuario #${user.id} cargado en el formulario (usa PUT).`);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    });

    document.querySelectorAll('[data-del]').forEach(btn => {
      btn.addEventListener('click', async () => {
        const id = Number(btn.getAttribute('data-del'));
        if(!confirm(`¿Eliminar usuario #${id}?`)) return;
        try{
          await api(`/users/${id}`, { method:'DELETE' });
          toast('Usuario eliminado', `DELETE /users/${id}`);
          // limpiar si estaba seleccionado
          const form = $('#formUser');
          if(Number(form.user_id.value) === id) form.user_id.value = '';
          await loadUsers();
        }catch(err){
          toast('No se pudo eliminar', err.message);
        }
      });
    });

  }catch(err){
    toast('Error cargando usuarios', err.message);
  }
}

$('#btnRefreshUsers').addEventListener('click', loadUsers);

// POST
$('#formUser').addEventListener('submit', async (e) => {
  e.preventDefault();
  const form = e.currentTarget;
  const payload = {
    name: form.name.value.trim(),
    role: form.role.value.trim(),
    active: !!form.active.checked
  };

  try{
    const data = await api('/users/', { method:'POST', body: JSON.stringify(payload) });
    toast('Usuario creado', `${data.user?.name || payload.name} (#${data.user?.id ?? '?'})`);
    form.reset();
    form.active.checked = true;
    form.user_id.value = '';
    await loadUsers();
  }catch(err){
    toast('No se pudo crear', err.message);
  }
});

// PUT
$('#btnUpdateUser').addEventListener('click', async () => {
  const form = $('#formUser');
  const id = Number(form.user_id.value);
  if(!id){
    toast('Falta ID', 'Escribe un ID para actualizar (PUT).');
    return;
  }

  const payload = {
    name: form.name.value.trim(),
    role: form.role.value.trim(),
    active: !!form.active.checked
  };

  try{
    await api(`/users/${id}`, { method:'PUT', body: JSON.stringify(payload) });
    toast('Usuario actualizado', `PUT /users/${id}`);
    await loadUsers();
  }catch(err){
    toast('No se pudo actualizar', err.message);
  }
});

// DELETE
$('#btnDeleteUser').addEventListener('click', async () => {
  const form = $('#formUser');
  const id = Number(form.user_id.value);
  if(!id){
    toast('Falta ID', 'Escribe un ID para eliminar (DELETE).');
    return;
  }
  if(!confirm(`¿Eliminar usuario #${id}?`)) return;

  try{
    await api(`/users/${id}`, { method:'DELETE' });
    toast('Usuario eliminado', `DELETE /users/${id}`);
    form.user_id.value = '';
    await loadUsers();
  }catch(err){
    toast('No se pudo eliminar', err.message);
  }
});

$('#btnSeedUsers').addEventListener('click', async () => {
  const sample = [
    { name:'Jesús', role:'Supervisor', active:true },
    { name:'Ana', role:'Operador', active:true },
    { name:'Luis', role:'Inventarios', active:false }
  ];
  for(const s of sample){
    try{ await api('/users/', { method:'POST', body: JSON.stringify(s) }); }
    catch{}
  }
  toast('Ejemplos', 'Usuarios de ejemplo cargados.');
  loadUsers();
});

// Packages
async function loadPackages(){
  try{
    const data = await api('/packages/');
    const items = data.items || [];
    fillTable('packagesTbody', items.map(p => (
      `<tr>
        <td>${p.id ?? ''}</td>
        <td>${escapeHtml(p.description ?? '')}</td>
        <td>${escapeHtml(p.origin ?? '')}</td>
        <td>${escapeHtml(p.created_at ?? p.date ?? '')}</td>
      </tr>`
    )), 4);
  }catch(err){
    toast('Error cargando paquetes', err.message);
  }
}

$('#btnRefreshPackages').addEventListener('click', loadPackages);

$('#formPackage').addEventListener('submit', async (e) => {
  e.preventDefault();
  const form = e.currentTarget;
  const payload = {
    description: form.description.value.trim(),
    origin: form.origin.value.trim()
  };

  try{
    const data = await api('/packages/', { method:'POST', body: JSON.stringify(payload) });
    toast('Paquete registrado', `#${data.package?.id ?? '?'} • ${payload.description}`);
    form.reset();
    await loadPackages();
  }catch(err){
    toast('No se pudo registrar', err.message);
  }
});

$('#btnSeedPackages').addEventListener('click', async () => {
  const sample = [
    { description:'Caja con playeras', origin:'Tijuana' },
    { description:'Bolsa de pantalones', origin:'Ensenada' },
    { description:'Lote de chamarras', origin:'Mexicali' }
  ];
  for(const s of sample){
    try{ await api('/packages/', { method:'POST', body: JSON.stringify(s) }); }
    catch{}
  }
  toast('Ejemplos', 'Paquetes de ejemplo cargados.');
  loadPackages();
});

// Attendance
async function loadAttendance(){
  try{
    const data = await api('/attendance/');
    const items = data.items || [];
    fillTable('attendanceTbody', items.map(a => (
      `<tr>
        <td>${a.id ?? ''}</td>
        <td>${a.user_id ?? ''}</td>
        <td>${escapeHtml(a.action ?? '')}</td>
        <td>${escapeHtml(a.timestamp ?? a.created_at ?? '')}</td>
      </tr>`
    )), 4);
  }catch(err){
    toast('Error cargando asistencia', err.message);
  }
}

$('#btnRefreshAttendance').addEventListener('click', loadAttendance);

$('#formAttendance').addEventListener('submit', async (e) => {
  e.preventDefault();
  const form = e.currentTarget;
  const payload = {
    user_id: Number(form.user_id.value),
    action: form.action.value
  };

  try{
    await api('/attendance/', { method:'POST', body: JSON.stringify(payload) });
    toast('Asistencia', `Registrado ${payload.action} para user_id=${payload.user_id}`);
    await loadAttendance();
  }catch(err){
    toast('No se pudo registrar', err.message);
  }
});

$('#btnQuickIn').addEventListener('click', async () => {
  try{
    await api('/attendance/', { method:'POST', body: JSON.stringify({ user_id: 1, action:'check-in' }) });
    toast('Asistencia', 'check-in (ID 1)');
    loadAttendance();
  }catch(err){
    toast('Error', err.message);
  }
});

$('#btnQuickOut').addEventListener('click', async () => {
  try{
    await api('/attendance/', { method:'POST', body: JSON.stringify({ user_id: 1, action:'check-out' }) });
    toast('Asistencia', 'check-out (ID 1)');
    loadAttendance();
  }catch(err){
    toast('Error', err.message);
  }
});

// Init
(async function init(){
  await loadHealth();
  await Promise.all([loadUsers(), loadPackages(), loadAttendance()]);
})();
