"""Main entry point for the app.

This app is generated based on your prompt in Vertex AI Studio using
Google GenAI Python SDK (https://googleapis.github.io/python-genai/) and
Gradio (https://www.gradio.app/).

You can customize the app by editing the code in Cloud Run source code editor.
You can also update the prompt in Vertex AI Studio and redeploy it.
"""

import base64
from google import genai
from google.genai import types
import gradio as gr
import utils


def generate(
    message,
    history: list[gr.ChatMessage],
    viewId,
    statusClass,
    type,
    status,
    request: gr.Request
):
  """Function to call the model based on the request."""

  validate_key_result = utils.validate_key(request)
  if validate_key_result is not None:
    yield validate_key_result
    return

  client = genai.Client(
      vertexai=True,
      project="studio-742957673-c3c93",
      location="global",
  )
  msg1_text1 = types.Part.from_text(text=f"""Help me build the followig CMS: 

<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Documentary Content Management System</title>
  <script src=\"https://cdn.tailwindcss.com\"></script>
  <script src=\"https://cdn.jsdelivr.net/npm/chart.js\"></script>
  <link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">
  <!-- Chosen Palette: Warm Neutrals -->
  <!-- Application Structure Plan: The application is designed as a task-oriented single-page application, moving beyond the report's sheet-based structure. The primary user flow starts at a high-level Dashboard for quick insights. Users can then navigate to dedicated views: the Content Hub (for managing assets, rights, and usage in an integrated manner), Financials (for billing), and a Workflow guide. This structure was chosen to align with user tasks (e.g., \"find an asset and see everything about it\") rather than data silos (viewing one sheet at a time). This improves efficiency by consolidating related information and reducing the need to cross-reference different sections. An interactive modal in the Content Hub is the centerpiece, linking data from three source sheets into a single, comprehensive view for any selected asset. -->
  <!-- Visualization & Content Choices: Report Info: Dashboard stats -> Goal: Inform -> Viz/Presentation: KPI Cards & Charts (Chart.js) -> Interaction: Hover tooltips -> Justification: Provides a quick, visual summary of project health. Report Info: Content, Rights, Usage Logs -> Goal: Organize & Relate -> Viz/Presentation: Interactive HTML table with a detail modal -> Interaction: Search, filter, row click to open modal -> Justification: The table allows efficient management of a large dataset, while the modal consolidates related information from three separate logs into one unified, easy-to-understand view. Report Info: Billing Tracker -> Goal: Organize -> Viz/Presentation: Filterable HTML table -> Interaction: Filter by status -> Justification: Simplifies tracking of financial obligations. Report Info: Recommended Workflow -> Goal: Inform -> Viz/Presentation: HTML/CSS step-by-step diagram -> Interaction: Static -> Justification: A visual guide is more intuitive and easier to follow than a text list. -->
  <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
  <style>
    body {{
      font-family: 'Inter', sans-serif;
      background-color: #FDFBF8;
      color: #4A4A4A;
    }}
    .nav-link {{
      transition: all 0.3s ease;
      border-bottom: 2px solid transparent;
    }}
    .nav-link.active {{
      border-bottom-color: #A58D78;
      color: #A58D78;
    }}
    .kpi-card {{
      background-color: #FFFFFF;
      border: 1px solid #EAEAEA;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .kpi-card:hover {{
      transform: translateY(-5px);
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }}
    .table-header {{
      background-color: #F7F5F2;
    }}
    .table-row:hover {{
      background-color: #F7F5F2;
    }}
    .modal-backdrop {{
      background-color: rgba(0, 0, 0, 0.5);
    }}
    .modal-content {{
      background-color: #FFFFFF;
    }}
    ::-webkit-scrollbar {{
      width: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: #F7F5F2;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #D1C7BD;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #A58D78;
    }}
    .chart-container {{
      position: relative;
      width: 100%;
      max-width: 500px;
      margin-left: auto;
      margin-right: auto;
      height: 320px;
      max-height: 400px;
    }}
    @media (min-width: 768px) {{
      .chart-container {{
        height: 380px;
      }}
    }}
  </style>
</head>
<body class=\"antialiased\">

  <div id=\"app\" class=\"min-h-screen\">
    <header class=\"bg-white/80 backdrop-blur-md shadow-sm sticky top-0 z-20\">
      <div class=\"container mx-auto px-4 sm:px-6 lg:px-8\">
        <div class=\"flex justify-between items-center py-4\">
          <h1 class=\"text-2xl font-bold text-gray-800\">Documentary CMS</h1>
          <nav class=\"hidden md:flex space-x-8\">
            <a href=\"#dashboard\" class=\"nav-link text-gray-600 hover:text-gray-900 font-medium pb-1\">Dashboard</a>
            <a href=\"#content-hub\" class=\"nav-link text-gray-600 hover:text-gray-900 font-medium pb-1\">Content Hub</a>
            <a href=\"#financials\" class=\"nav-link text-gray-600 hover:text-gray-900 font-medium pb-1\">Financials</a>
            <a href=\"#workflow\" class=\"nav-link text-gray-600 hover:text-gray-900 font-medium pb-1\">Workflow Guide</a>
          </nav>
          <div class=\"md:hidden\">
            <select id=\"mobile-nav\" class=\"block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50\">
              <option value=\"dashboard\">Dashboard</option>
              <option value=\"content-hub\">Content Hub</option>
              <option value=\"financials\">Financials</option>
              <option value=\"workflow\">Workflow</option>
            </select>
          </div>
        </div>
      </div>
    </header>

    <main class=\"container mx-auto p-4 sm:p-6 lg:p-8\">
      <div id=\"dashboard\" class=\"view\">
        <section id=\"dashboard-kpis\" class=\"grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8\">
        </section>
        <section class=\"grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8\">
          <div class=\"kpi-card rounded-xl shadow-lg p-6\">
            <h3 class=\"text-xl font-semibold mb-4 text-center\">License Status</h3>
            <div class=\"chart-container\">
              <canvas id=\"licenseStatusChart\"></canvas>
            </div>
          </div>
          <div class=\"kpi-card rounded-xl shadow-lg p-6\">
            <h3 class=\"text-xl font-semibold mb-4 text-center\">Content Types</h3>
            <div class=\"chart-container\">
              <canvas id=\"contentTypeChart\"></canvas>
            </div>
          </div>
        </section>
        <section class=\"kpi-card rounded-xl shadow-lg p-6\">
          <h3 class=\"text-xl font-semibold mb-4\">Actionable Items</h3>
          <div id=\"actionable-items-list\" class=\"space-y-4\"></div>
        </section>
      </div>
       
      <div id=\"content-hub\" class=\"view hidden\">
        <div class=\"bg-white p-6 rounded-xl shadow-lg\">
          <h2 class=\"text-2xl font-bold mb-4\">Content Hub</h2>
          <p class=\"mb-6 text-gray-600\">This is the central database for all content assets. Use the search and filter options to explore the log. Click on any row to see comprehensive details about the asset, its rights holder, and its specific usage in the film.</p>
          <div class=\"flex flex-col md:flex-row gap-4 mb-4\">
            <input type=\"text\" id=\"contentSearch\" placeholder=\"Search by title, ID, or description...\" class=\"flex-grow p-2 border rounded-md shadow-sm\">
            <select id=\"contentTypeFilter\" class=\"p-2 border rounded-md shadow-sm\">
              <option value=\"\">All Content Types</option>
            </select>
            <select id=\"licenseStatusFilter\" class=\"p-2 border rounded-md shadow-sm\">
              <option value=\"\">All License Statuses</option>
            </select>
          </div>
          <div class=\"overflow-x-auto\">
            <table class=\"w-full text-left\">
              <thead class=\"table-header\">
                <tr>
                  <th class=\"p-3\">Asset ID</th>
                  <th class=\"p-3\">Title</th>
                  <th class=\"p-3\">Content Type</th>
                  <th class=\"p-3\">License Status</th>
                  <th class=\"p-3\">Cost</th>
                </tr>
              </thead>
              <tbody id=\"contentLogTable\">
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div id=\"financials\" class=\"view hidden\">
        <div class=\"bg-white p-6 rounded-xl shadow-lg\">
          <h2 class=\"text-2xl font-bold mb-4\">Financials Overview</h2>
          <p class=\"mb-6 text-gray-600\">This section tracks all financial transactions related to content licensing. Monitor invoice statuses and manage payments to rights holders to ensure the project stays on budget and obligations are met.</p>
           <div class=\"flex flex-col md:flex-row gap-4 mb-4\">
            <select id=\"paymentStatusFilter\" class=\"p-2 border rounded-md shadow-sm\">
              <option value=\"\">All Payment Statuses</option>
              <option value=\"Paid\">Paid</option>
              <option value=\"Pending\">Pending</option>
              <option value=\"Overdue\">Overdue</option>
            </select>
          </div>
          <div class=\"overflow-x-auto\">
            <table class=\"w-full text-left\">
              <thead class=\"table-header\">
                <tr>
                  <th class=\"p-3\">Invoice ID</th>
                  <th class=\"p-3\">Rights Holder</th>
                  <th class=\"p-3\">Amount</th>
                  <th class=\"p-3\">Due Date</th>
                  <th class=\"p-3\">Status</th>
                </tr>
              </thead>
              <tbody id=\"billingTable\">
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div id=\"workflow\" class=\"view hidden\">
        <div class=\"bg-white p-6 rounded-xl shadow-lg\">
          <h2 class=\"text-2xl font-bold mb-6\">Recommended Workflow</h2>
          <p class=\"mb-8 text-gray-600\">This guide outlines the standard operating procedure for managing content from acquisition to final payment. Following this workflow ensures data integrity, proper rights clearance, and efficient project management.</p>
          <div id=\"workflow-steps\" class=\"space-y-8\">
          </div>
        </div>
      </div>
    </main>
  </div>

  <div id=\"assetDetailModal\" class=\"fixed inset-0 z-30 hidden items-center justify-center p-4 modal-backdrop\">
    <div class=\"modal-content max-w-4xl w-full max-h-[90vh] rounded-xl shadow-2xl flex flex-col\">
      <div class=\"p-6 flex justify-between items-center border-b\">
        <h3 id=\"modalTitle\" class=\"text-2xl font-bold\">Asset Details</h3>
        <button id=\"closeModal\" class=\"text-3xl font-light leading-none\">&times;</button>
      </div>
      <div class=\"p-6 overflow-y-auto\" id=\"modalBody\">
      </div>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', function () {{
       
      const sampleData = {{
        contentLog: [
          {{ id: 'VID-001', title: 'Times Square Opening Shot', desc: '4K drone footage of Times Square at dawn.', type: 'Archival Footage', source: 'Stock Footage Inc.', rightsHolderId: 'RH-001', status: 'Cleared', licenseType: 'Rights-Managed', cost: 1500, restrictions: 'Worldwide, 10 years, all media.', acquired: '2025-09-10', location: '/assets/VID-001.mov', notes: '' }},
          {{ id: 'PHO-001', title: 'Protest March on Main St.', desc: 'B&W photo of protestors.', type: 'Photo', source: 'National Archives', rightsHolderId: 'RH-002', status: 'Public Domain', licenseType: 'Public Domain', cost: 0, restrictions: 'None', acquired: '2025-09-15', location: '/assets/PHO-001.tif', notes: 'Requires \"Courtesy of National Archives\" credit.' }},
          {{ id: 'AUD-001', title: 'Interview with Dr. Evans', desc: 'Audio recording of expert interview.', type: 'Audio', source: 'Production Team', rightsHolderId: 'RH-003', status: 'Cleared', licenseType: 'Custom', cost: 250, restrictions: 'Film use only.', acquired: '2025-09-20', location: '/assets/AUD-001.wav', notes: 'Release form signed.' }},
          {{ id: 'DOC-001', title: 'Declassified Government Memo', desc: 'Scanned PDF of a 1972 memo.', type: 'Document', source: 'FOIA Request', rightsHolderId: 'RH-002', status: 'Public Domain', licenseType: 'Public Domain', cost: 0, restrictions: 'None', acquired: '2025-09-22', location: '/assets/DOC-001.pdf', notes: '' }},
          {{ id: 'VID-002', title: 'Factory Floor Footage', desc: '1950s archival film of an assembly line.', type: 'Archival Footage', source: 'Archive Films', rightsHolderId: 'RH-004', status: 'Pending', licenseType: 'Rights-Managed', cost: 800, restrictions: 'TBD', acquired: '2025-10-01', location: '/assets/VID-002.mp4', notes: 'Negotiating terms.' }},
          {{ id: 'PHO-002', title: 'Family Portrait', desc: 'Color photo of the main subject\\'s family.', type: 'Photo', source: 'Subject\\'s Collection', rightsHolderId: 'RH-005', status: 'To Be Negotiated', licenseType: 'Custom', cost: 100, restrictions: 'TBD', acquired: '2025-10-03', location: '/assets/PHO-002.jpg', notes: 'Need to contact family for release.' }},
        ],
        rightsHolders: [
          {{ id: 'RH-001', name: 'Stock Footage Inc.', contact: 'Sales Dept.', email: 'sales@stock.com', phone: '111-222-3333', address: '123 Media Way, Hollywood, CA', payment: 'Wire Transfer: 123456789' }},
          {{ id: 'RH-002', name: 'National Archives', contact: 'Public Domain Office', email: 'info@archives.gov', phone: 'N/A', address: 'Washington D.C.', payment: 'N/A' }},
          {{ id: 'RH-003', name: 'Dr. Alana Evans', contact: '', email: 'a.evans@university.edu', phone: '222-333-4444', address: '456 College Ave, Boston, MA', payment: 'Check' }},
          {{ id: 'RH-004', name: 'Archive Films', contact: 'Licensing Team', email: 'license@archivefilms.com', phone: '333-444-5555', address: '789 History Lane, New York, NY', payment: 'PayPal: payments@archive.com' }},
          {{ id: 'RH-005', name: 'The Miller Family Estate', contact: 'John Miller', email: 'jmiller@email.com', phone: '444-555-6666', address: '101 Family Rd, Chicago, IL', payment: 'TBD' }},
        ],
        usageLog: [
          {{ id: 'USE-001', assetId: 'VID-001', scene: 1, sequence: 'Opening Montage', in: '00:00:05:10', out: '00:00:12:00', type: 'B-Roll' }},
          {{ id: 'USE-002', assetId: 'PHO-001', scene: 5, sequence: 'The Protest Era', in: '00:15:32:10', out: '00:15:38:05', type: 'On-Screen Graphic' }},
          {{ id: 'USE-003', assetId: 'AUD-001', scene: 5, sequence: 'The Protest Era', in: '00:15:30:00', out: '00:18:00:00', type: 'Voice Over' }},
          {{ id: 'USE-004', assetId: 'VID-001', scene: 20, sequence: 'Closing Credits', in: '01:28:15:00', out: '01:28:20:00', type: 'Background' }},
        ],
        billing: [
          {{ id: 'INV-001', holderId: 'RH-001', assets: 'VID-001', amount: 1500, date: '2025-09-12', due: '2025-10-12', status: 'Paid', paidDate: '2025-10-10' }},
          {{ id: 'INV-002', holderId: 'RH-003', assets: 'AUD-001', amount: 250, date: '2025-09-25', due: '2025-10-25', status: 'Pending', paidDate: '' }},
          {{ id: 'INV-003', holderId: 'RH-004', assets: 'VID-002', amount: 800, date: '2025-10-02', due: '2025-11-01', status: 'Pending', paidDate: '' }},
        ]
      }};

      const appState = {{
        currentView: 'dashboard',
        charts: {{}},
        filters: {{
          contentSearch: '',
          contentType: '',
          licenseStatus: '',
          paymentStatus: ''
        }}
      }};

      const views = document.querySelectorAll('.view');
      const navLinks = document.querySelectorAll('.nav-link');
      const mobileNav = document.getElementById('mobile-nav');

      function navigateTo(viewId) {{
        appState.currentView = viewId;
        views.forEach(view => view.classList.add('hidden'));
        document.getElementById(viewId).classList.remove('hidden');

        navLinks.forEach(link => {{
          if (link.getAttribute('href') === `#${viewId}`) {{
            link.classList.add('active');
          }} else {{
            link.classList.remove('active');
          }}
        }});
        mobileNav.value = viewId;
      }}

      navLinks.forEach(link => {{
        link.addEventListener('click', (e) => {{
          e.preventDefault();
          const viewId = link.getAttribute('href').substring(1);
          navigateTo(viewId);
        }});
      }});

      mobileNav.addEventListener('change', (e) => {{
        navigateTo(e.target.value);
      }});
       
      window.addEventListener('hashchange', () => {{
        const viewId = window.location.hash.substring(1) || 'dashboard';
        navigateTo(viewId);
      }});
       
      function renderDashboardKPIs() {{
        const totalAssets = sampleData.contentLog.length;
        const totalCost = sampleData.contentLog.reduce((sum, item) => sum + item.cost, 0);
        const totalPaid = sampleData.billing.filter(b => b.status === 'Paid').reduce((sum, item) => sum + item.amount, 0);
        const outstanding = totalCost - totalPaid;

        const kpis = [
          {{ label: 'Total Assets Logged', value: totalAssets, icon: '🗂️' }},
          {{ label: 'Total Licensed Cost', value: `$${{totalCost.toLocaleString()}}`, icon: '💰' }},
          {{ label: 'Total Paid', value: `$${{totalPaid.toLocaleString()}}`, icon: '✅' }},
          {{ label: 'Outstanding Payments', value: `$${{outstanding.toLocaleString()}}`, icon: '⏳' }},
        ];

        const container = document.getElementById('dashboard-kpis');
        container.innerHTML = kpis.map(kpi => `
          <div class=\"kpi-card rounded-xl shadow-lg p-6 flex items-center\">
            <div class=\"text-4xl mr-4\">${{kpi.icon}}</div>
            <div>
              <div class=\"text-3xl font-bold\">${{kpi.value}}</div>
              <div class=\"text-gray-500\">${{kpi.label}}</div>
            </div>
          </div>
        `).join('');
      }}
       
      function renderDashboardCharts() {{
        const licenseStatusCtx = document.getElementById('licenseStatusChart').getContext('2d');
        const contentTypeCtx = document.getElementById('contentTypeChart').getContext('2d');

        const statusCounts = sampleData.contentLog.reduce((acc, item) => {{
          acc[item.status] = (acc[item.status] || 0) + 1;
          return acc;
        }}, {{}});

        const typeCounts = sampleData.contentLog.reduce((acc, item) => {{
          acc[item.type] = (acc[item.type] || 0) + 1;
          return acc;
        }}, {{}});
         
        const pieColors = ['#4CAF50', '#FFC107', '#F44336', '#9E9E9E', '#2196F3'];
        const barColors = ['#A58D78', '#C3B6A9', '#E1D9CF', '#F7F5F2', '#6B5B4B'];

        if (appState.charts.licenseStatus) appState.charts.licenseStatus.destroy();
        appState.charts.licenseStatus = new Chart(licenseStatusCtx, {{
          type: 'doughnut',
          data: {{
            labels: Object.keys(statusCounts),
            datasets: [{{ data: Object.values(statusCounts), backgroundColor: pieColors }}]
          }},
          options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ position: 'bottom' }} }} }}
        }});

        if (appState.charts.contentType) appState.charts.contentType.destroy();
        appState.charts.contentType = new Chart(contentTypeCtx, {{
          type: 'bar',
          data: {{
            labels: Object.keys(typeCounts),
            datasets: [{{ label: 'Count', data: Object.values(typeCounts), backgroundColor: barColors }}]
          }},
          options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ display: false }} }} }}
        }});
      }}

      function renderActionableItems() {{
        const container = document.getElementById('actionable-items-list');
        const pendingClearance = sampleData.contentLog.filter(item => item.status === 'Pending' || item.status === 'To Be Negotiated');
        const upcomingPayments = sampleData.billing.filter(b => b.status === 'Pending' && new Date(b.due) > new Date());
         
        let html = '<div><h4 class=\"font-semibold text-lg mb-2\">Assets Pending Clearance</h4>';
        if (pendingClearance.length > 0) {{
          html += `<ul class=\"list-disc pl-5 space-y-1\">${{pendingClearance.map(item => `<li>${{item.id}} - ${{item.title}} (${{item.status}})</li>`).join('')}}</ul>`;
        }} else {{
          html += '<p class=\"text-gray-500\">All assets cleared.</p>';
        }}
        html += '</div>';

        html += '<div class=\"mt-6\"><h4 class=\"font-semibold text-lg mb-2\">Upcoming Payments</h4>';
        if (upcomingPayments.length > 0) {{
          html += `<ul class=\"list-disc pl-5 space-y-1\">${{upcomingPayments.map(item => `<li>${{item.id}} - $${{item.amount}} due on ${{item.due}}</li>`).join('')}}</ul>`;
        }} else {{
          html += '<p class=\"text-gray-500\">No upcoming payments.</p>';
        }}
        html += '</div>';
        container.innerHTML = html;
      }}

      function renderContentLogTable() {{
        const tbody = document.getElementById('contentLogTable');
        const {{ contentSearch, contentType, licenseStatus }} = appState.filters;
         
        const filteredData = sampleData.contentLog.filter(item => {{
          const searchMatch = contentSearch.toLowerCase() === '' ||
                   item.title.toLowerCase().includes(contentSearch) ||
                   item.id.toLowerCase().includes(contentSearch) ||
                   item.desc.toLowerCase().includes(contentSearch);
          const typeMatch = contentType === '' || item.type === contentType;
          const statusMatch = licenseStatus === '' || item.status === licenseStatus;
          return searchMatch && typeMatch && statusMatch;
        }});

        tbody.innerHTML = filteredData.map(item => `
          <tr class=\"table-row cursor-pointer\" data-id=\"${{item.id}}\">
            <td class=\"p-3 font-mono text-sm\">${{item.id}}</td>
            <td class=\"p-3 font-medium\">${{item.title}}</td>
            <td class=\"p-3\">${{item.type}}</td>
            <td class=\"p-3\">${{item.status}}</td>
            <td class=\"p-3\">$${{item.cost.toLocaleString()}}</td>
          </tr>
        `).join('');
         
        document.querySelectorAll('#contentLogTable tr').forEach(row => {{
          row.addEventListener('click', () => showAssetDetailModal(row.dataset.id));
        }});
      }}
       
      function renderBillingTable() {{
        const tbody = document.getElementById('billingTable');
        const {{ paymentStatus }} = appState.filters;

        const filteredData = sampleData.billing.filter(item => {{
          return paymentStatus === '' || item.status === paymentStatus;
        }});

        tbody.innerHTML = filteredData.map(item => {{
           const holder = sampleData.rightsHolders.find(h => h.id === item.holderId);
           let statusClass = 'bg-yellow-100 text-yellow-800';
           if (item.status === 'Paid') statusClass = 'bg-green-100 text-green-800';
           if (item.status === 'Overdue' || (new Date(item.due) < new Date() && item.status !== 'Paid')) statusClass = 'bg-red-100 text-red-800';
          return `
            <tr class=\"table-row\">
              <td class=\"p-3 font-mono text-sm\">${{item.id}}</td>
              <td class=\"p-3 font-medium\">${{holder ? holder.name : 'N/A'}}</td>
              <td class=\"p-3\">$${{item.amount.toLocaleString()}}</td>
              <td class=\"p-3\">${{item.due}}</td>
              <td class=\"p-3\"><span class=\"px-2 py-1 text-xs font-semibold rounded-full ${statusClass}\">${{item.status}}</span></td>
            </tr>
          `
        }}).join('');
      }}
       
      function setupFilters() {{
        const contentTypes = [...new Set(sampleData.contentLog.map(item => item.type))];
        const licenseStatuses = [...new Set(sampleData.contentLog.map(item => item.status))];
         
        const contentTypeFilter = document.getElementById('contentTypeFilter');
        contentTypes.forEach(type => {{
          contentTypeFilter.innerHTML += `<option value=\"${type}\">${type}</option>`;
        }});
         
        const licenseStatusFilter = document.getElementById('licenseStatusFilter');
        licenseStatuses.forEach(status => {{
          licenseStatusFilter.innerHTML += `<option value=\"${status}\">${status}</option>`;
        }});
         
        document.getElementById('contentSearch').addEventListener('input', e => {{
          appState.filters.contentSearch = e.target.value.toLowerCase();
          renderContentLogTable();
        }});
        contentTypeFilter.addEventListener('change', e => {{
          appState.filters.contentType = e.target.value;
          renderContentLogTable();
        }});
        licenseStatusFilter.addEventListener('change', e => {{
          appState.filters.licenseStatus = e.target.value;
          renderContentLogTable();
        }});
        document.getElementById('paymentStatusFilter').addEventListener('change', e => {{
          appState.filters.paymentStatus = e.target.value;
          renderBillingTable();
        }});
      }}
       
      function renderWorkflow() {{
        const steps = [
          {{ title: 'Acquisition', desc: 'New content is found and logged in the Content Hub with a \"Pending\" status.', icon: '📥' }},
          {{ title: 'Rights Holder Entry', desc: 'If new, the content owner is added to the system via the Content Hub.', icon: '👤' }},
          {{ title: 'Clearance', desc: 'Negotiate rights. Update license status, cost, and restrictions in the asset\\'s details.', icon: '✍️' }},
          {{ title: 'Editing', desc: 'When an asset is used in the edit, log the usage details (timecodes, scene) in its record.', icon: '🎬' }},
          {{ title: 'Billing', desc: 'Record received invoices in the Financials section.', icon: '🧾' }},
          {{ title: 'Payment & Monitoring', desc: 'Track and update payment status. Use the Dashboard to monitor overall project health.', icon: '📊' }}
        ];
        const container = document.getElementById('workflow-steps');
        container.innerHTML = steps.map((step, index) => `
          <div class=\"flex items-start\">
            <div class=\"flex-shrink-0 flex flex-col items-center mr-6\">
              <div class=\"bg-gray-200 rounded-full h-12 w-12 flex items-center justify-center text-2xl\">${{step.icon}}</div>
              ${{index < steps.length - 1 ? '<div class=\"w-px h-16 bg-gray-300 mt-2\"></div>' : ''}}
            </div>
            <div>
              <h4 class=\"text-lg font-semibold\">${{index + 1}}. ${{step.title}}</h4>
              <p class=\"text-gray-600\">${{step.desc}}</p>
            </div>
          </div>
        `).join('');
      }}
       
      const modal = document.getElementById('assetDetailModal');
      function showAssetDetailModal(assetId) {{
        const asset = sampleData.contentLog.find(item => item.id === assetId);
        if (!asset) return;

        const holder = sampleData.rightsHolders.find(h => h.id === asset.rightsHolderId);
        const usages = sampleData.usageLog.filter(u => u.assetId === assetId);

        document.getElementById('modalTitle').textContent = `${{asset.id}}: ${{asset.title}}`;
        const body = document.getElementById('modalBody');
        body.innerHTML = `
          <div class=\"grid grid-cols-1 md:grid-cols-2 gap-8\">
            <div>
              <h4 class=\"text-lg font-semibold border-b pb-2 mb-3\">Asset Information</h4>
              <div class=\"space-y-2 text-sm\">
                <p><strong>Description:</strong> ${{asset.desc}}</p>
                <p><strong>Content Type:</strong> ${{asset.type}}</p>
                <p><strong>Source:</strong> ${{asset.source}}</p>
                <p><strong>Date Acquired:</strong> ${{asset.acquired}}</p>
                <p><strong>File Location:</strong> <code class=\"text-xs bg-gray-100 p-1 rounded\">${{asset.location}}</code></p>
                <p><strong>Notes:</strong> ${{asset.notes || 'None'}}</p>
              </div>
               <h4 class=\"text-lg font-semibold border-b pb-2 mb-3 mt-6\">License Details</h4>
              <div class=\"space-y-2 text-sm\">
                <p><strong>Status:</strong> ${{asset.status}}</p>
                <p><strong>License Type:</strong> ${{asset.licenseType}}</p>
                <p><strong>Cost:</strong> $${{asset.cost.toLocaleString()}}</p>
                <p><strong>Restrictions:</strong> ${{asset.restrictions}}</p>
              </div>
            </div>
            <div>
              <h4 class=\"text-lg font-semibold border-b pb-2 mb-3\">Rights Holder</h4>
              ${{holder ? `
              <div class=\"space-y-2 text-sm bg-gray-50 p-4 rounded-lg\">
                <p><strong>ID:</strong> ${{holder.id}}</p>
                <p><strong>Name:</strong> ${{holder.name}}</p>
                <p><strong>Contact:</strong> ${{holder.contact || 'N/A'}}</p>
                <p><strong>Email:</strong> ${{holder.email}}</p>
                <p><strong>Payment Details:</strong> ${{holder.payment}}</p>
              </div>
              ` : '<p class=\"text-sm\">No rights holder information available.</p>'}}
               
              <h4 class=\"text-lg font-semibold border-b pb-2 mb-3 mt-6\">Usage Log (${{usages.length}})</h4>
               ${{usages.length > 0 ? `
              <div class=\"space-y-3 text-sm\">
                ${{usages.map(u => `
                  <div class=\"bg-gray-50 p-3 rounded-lg\">
                    <p><strong>Sequence:</strong> ${{u.sequence}}</p>
                    <p><strong>Timecode:</strong> ${{u.in}} - ${{u.out}}</p>
                    <p><strong>Usage Type:</strong> ${{u.type}}</p>
                  </div>
                `).join('')}}
              </div>
              ` : '<p class=\"text-sm\">This asset has not been used in the edit yet.</p>'}}
            </div>
          </div>
        `;
        modal.classList.remove('hidden');
        modal.classList.add('flex');
      }}

      document.getElementById('closeModal').addEventListener('click', () => {{
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }});
      modal.addEventListener('click', (e) => {{
        if (e.target === modal) {{
          modal.classList.add('hidden');
          modal.classList.remove('flex');
        }}
      }});

      function initializeApp() {{
        renderDashboardKPIs();
        renderDashboardCharts();
        renderActionableItems();
        setupFilters();
        renderContentLogTable();
        renderBillingTable();
        renderWorkflow();
         
        const initialView = window.location.hash.substring(1) || 'dashboard';
        navigateTo(initialView);
      }}

      initializeApp();
    }});
  </script>
</body>
</html>""")


  model = "gemini-2.5-flash-preview-09-2025"
  contents = [
    types.Content(
      role="user",
      parts=[
        msg1_text1
      ]
    ),
  ]

  for prev_msg in history:
    role = "user" if prev_msg["role"] == "user" else "model"
    parts = utils.get_parts_from_message(prev_msg["content"])
    if parts:
      contents.append(types.Content(role=role, parts=parts))

  if message:
    contents.append(
        types.Content(role="user", parts=utils.get_parts_from_message(message))
    )

  generate_content_config = types.GenerateContentConfig(
      temperature=1,
      top_p=0.95,
      max_output_tokens=65535,
      safety_settings=[
          types.SafetySetting(
              category="HARM_CATEGORY_HATE_SPEECH",
              threshold="OFF"
          ),
          types.SafetySetting(
              category="HARM_CATEGORY_DANGEROUS_CONTENT",
              threshold="OFF"
          ),
          types.SafetySetting(
              category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
              threshold="OFF"
          ),
          types.SafetySetting(
              category="HARM_CATEGORY_HARASSMENT",
              threshold="OFF"
          )
      ],
  )

  results = []
  for chunk in client.models.generate_content_stream(
      model=model,
      contents=contents,
      config=generate_content_config,
  ):
    if chunk.candidates and chunk.candidates[0] and chunk.candidates[0].content:
      results.extend(
          utils.convert_content_to_gr_type(chunk.candidates[0].content)
      )
      if results:
        yield results

with gr.Blocks() as demo:
  with gr.Row():
    gr.HTML(utils.public_access_warning)
  with gr.Row():
    with gr.Column(scale=1):
      with gr.Row():
        gr.HTML("<h2>Welcome to Vertex AI GenAI App!</h2>")
      with gr.Row():
        gr.HTML("""This prototype was built using your Vertex AI Studio prompt.
            Follow the steps and recommendations below to begin.""")
      with gr.Row():
        gr.HTML(utils.next_steps_html)

    with gr.Column(scale=2, variant="panel"):
      gr.ChatInterface(
          fn=generate,
          title="Build a Documentary CMS</answer>",
          multimodal=True,
          additional_inputs=[
              gr.Textbox(label="viewId"),
              gr.Textbox(label="statusClass"),
              gr.Textbox(label="type"),
              gr.Textbox(label="status"),
          ],
          flagging_mode="never",
      )
if __name__ == "__main__":
    demo.launch(
      server_name="0.0.0.0",
      server_port=7860,
      theme=utils.custom_theme
    )