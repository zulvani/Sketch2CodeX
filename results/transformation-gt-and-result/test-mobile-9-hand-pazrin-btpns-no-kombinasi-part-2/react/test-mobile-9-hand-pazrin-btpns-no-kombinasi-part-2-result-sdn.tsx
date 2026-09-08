import './App.css'

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-0">
      <div className="mx-auto max-w-md rounded bg-white p-6 shadow">

        {/* Row 1 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-11 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping alert */}<div obj="alert">
                  <div className="w-full rounded border border-amber-300 bg-amber-50 px-4 py-3 text-amber-900">
                <div className="flex items-start gap-2">
                  <span className="text-lg leading-none">!</span>
                  <div>Alert</div>
                </div>
              </div>

</div>
            </div>
          </div>
        </div>

        {/* Row 2 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-11 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping key-value */}<div obj="key-value">
                  <table className="w-full table-fixed border-collapse">
                <thead>
                  <tr>
                    <th className="border p-2 text-left">Header 1</th>
                    <th className="border p-2 text-left">Header 2</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td className="border p-2">Cell 1</td>
                    <td className="border p-2">Cell 2</td>
                  </tr>
                </tbody>
              </table>

</div>
            </div>
          </div>
        </div>

        {/* Row 3 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-3 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping switch */}<div obj="switch">
                  <label className="inline-flex items-center gap-2">
                <input type="checkbox" className="sr-only" />
                <span className="w-10 h-5 bg-gray-300 rounded-full"></span>
              </label>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-5 col-start-4">
            <div className="flex gap-2">
{/* Object Mapping date-picker */}<div obj="date-picker">
                  <input type="date" className="w-full rounded border p-2" />

</div>
            </div>
          </div>
        </div>

        {/* Row 4 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-2 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping switch */}<div obj="switch">
                  <label className="inline-flex items-center gap-2">
                <input type="checkbox" className="sr-only" />
                <span className="w-10 h-5 bg-gray-300 rounded-full"></span>
              </label>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-8 col-start-4">
            <div className="flex gap-2">
{/* Object Mapping input-free-text */}<div obj="input-free-text">
                  <input
                type="text"
                placeholder="Enter text"
                className="w-full rounded border p-2"
              />

</div>
            </div>
          </div>
        </div>

        {/* Row 5 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-2 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping bar-chart */}<div obj="bar-chart">
                  <div className="w-full h-40 flex items-center justify-center bg-gray-50 rounded">
                Chart
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-8 col-start-4">
            <div className="flex gap-2">
{/* Object Mapping input-password */}<div obj="input-password">
                  <input
                type="password"
                placeholder="Enter password"
                className="w-full rounded border p-2"
              />

</div>
            </div>
          </div>
        </div>

        {/* Row 6 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-2 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping switch */}<div obj="switch">
                  <label className="inline-flex items-center gap-2">
                <input type="checkbox" className="sr-only" />
                <span className="w-10 h-5 bg-gray-300 rounded-full"></span>
              </label>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-8 col-start-4">
            <div className="flex gap-2">
{/* Object Mapping input-password */}<div obj="input-password">
                  <input
                type="password"
                placeholder="Enter password"
                className="w-full rounded border p-2"
              />

</div>
            </div>
          </div>
        </div>

        {/* Row 7 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-2 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping label */}<div obj="label">
                  <label className="text-sm font-medium">
                Label
              </label>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-8 col-start-4">
            <div className="flex gap-2">
{/* Object Mapping input-password */}<div obj="input-password">
                  <input
                type="password"
                placeholder="Enter password"
                className="w-full rounded border p-2"
              />

</div>
            </div>
          </div>
        </div>

        {/* Row 8 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-3 col-start-3">
            <div className="flex gap-2">
{/* Object Mapping input-password */}<div obj="input-password">
                  <input
                type="password"
                placeholder="Enter password"
                className="w-full rounded border p-2"
              />

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-4 col-start-7">
            <div className="flex gap-2">
{/* Object Mapping input-password */}<div obj="input-password">
                  <input
                type="password"
                placeholder="Enter password"
                className="w-full rounded border p-2"
              />

</div>
            </div>
          </div>
        </div>

        {/* Row 9 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-8 col-start-3">
            <div className="flex gap-2">
{/* Object Mapping hyperlink */}<div obj="hyperlink">
                  <a href="#" className="text-blue-500 underline">
                Hyperlink
              </a>

</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  )
}
