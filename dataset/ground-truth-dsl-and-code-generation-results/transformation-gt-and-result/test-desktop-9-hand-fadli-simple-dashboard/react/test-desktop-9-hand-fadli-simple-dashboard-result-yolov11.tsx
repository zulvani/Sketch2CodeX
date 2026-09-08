import './App.css'

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-0">
      <div className="mx-auto  rounded bg-white p-6 shadow">

        {/* Row 1 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-4 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping label */}<div obj="label">
                  <label className="text-sm font-medium">
                Label
              </label>

</div>
            </div>
          </div>
        </div>

        {/* Row 2 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-3 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping date-picker */}<div obj="date-picker">
                  <input type="date" className="w-full rounded border p-2" />

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-5">
            <div className="flex gap-2">
{/* Object Mapping input-number */}<div obj="input-number">
                  <input
                type="number"
                placeholder="0"
                className="w-full rounded border p-2"
              />

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-9">
            <div className="flex gap-2">
{/* Object Mapping input-number */}<div obj="input-number">
                  <input
                type="number"
                placeholder="0"
                className="w-full rounded border p-2"
              />

</div>
            </div>
          </div>
        </div>

        {/* Row 3 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-10 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping line-chart */}<div obj="line-chart">
                  <div className="w-full h-40 flex items-center justify-center bg-gray-50 rounded">
                Chart
              </div>

</div>
            </div>
          </div>
        </div>

        {/* Row 4 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-3 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping bar-chart */}<div obj="bar-chart">
                  <div className="w-full h-40 flex items-center justify-center bg-gray-50 rounded">
                Chart
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-5">
            <div className="flex gap-2">
{/* Object Mapping pie-chart */}<div obj="pie-chart">
                  <div className="w-full h-40 flex items-center justify-center bg-gray-50 rounded">
                Chart
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-8">
            <div className="flex gap-2">
{/* Object Mapping icon-button */}<div obj="icon-button">
                  <button className="inline-flex items-center gap-2 rounded p-2 text-white bg-blue-500">
                <span className="text-lg">★</span>
              </button>

</div>
            </div>
            <div className="flex gap-2">
{/* Object Mapping icon-button */}<div obj="icon-button">
                  <button className="inline-flex items-center gap-2 rounded p-2 text-white bg-blue-500">
                <span className="text-lg">★</span>
              </button>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-10">
            <div className="flex gap-2">
{/* Object Mapping icon-button */}<div obj="icon-button">
                  <button className="inline-flex items-center gap-2 rounded p-2 text-white bg-blue-500">
                <span className="text-lg">★</span>
              </button>

</div>
            </div>
            <div className="flex gap-2">
{/* Object Mapping icon-button */}<div obj="icon-button">
                  <button className="inline-flex items-center gap-2 rounded p-2 text-white bg-blue-500">
                <span className="text-lg">★</span>
              </button>

</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  )
}
