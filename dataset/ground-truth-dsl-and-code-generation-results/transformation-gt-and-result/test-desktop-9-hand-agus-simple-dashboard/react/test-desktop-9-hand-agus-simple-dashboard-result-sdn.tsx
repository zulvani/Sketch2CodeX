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
          <div class="v-col" className="col-span-3 col-start-4">
            <div className="flex gap-2">
{/* Object Mapping combobox */}<div obj="combobox">
                  <select className="w-full rounded border p-2">
                <option>Option 1</option>
                <option>Option 2</option>
              </select>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-7">
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
          <div class="v-col" className="col-span-12 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping common-button */}<div obj="common-button">
                  <button className="w-full rounded bg-blue-500 px-4 py-2 text-white">
                Button
              </button>

</div>
            </div>
          </div>
        </div>

        {/* Row 4 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-4 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping checkbox */}<div obj="checkbox">
                  <input type="checkbox" className="h-5 w-5" />

</div>
{/* Object Mapping pie-chart */}<div obj="pie-chart">
                  <div className="w-full h-40 flex items-center justify-center bg-gray-50 rounded">
                Chart
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-9">
            <div className="flex gap-2">
{/* Object Mapping image */}<div obj="image">
                  <div className="flex w-full items-center justify-center">
                <div className="w-full h-40 bg-gray-100 rounded bg-center bg-cover flex items-center justify-center">Image</div>
              </div>

</div>
            </div>
            <div className="flex gap-2">
{/* Object Mapping image */}<div obj="image">
                  <div className="flex w-full items-center justify-center">
                <div className="w-full h-40 bg-gray-100 rounded bg-center bg-cover flex items-center justify-center">Image</div>
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-2 col-start-11">
            <div className="flex gap-2">
{/* Object Mapping image */}<div obj="image">
                  <div className="flex w-full items-center justify-center">
                <div className="w-full h-40 bg-gray-100 rounded bg-center bg-cover flex items-center justify-center">Image</div>
              </div>

</div>
            </div>
            <div className="flex gap-2">
{/* Object Mapping image */}<div obj="image">
                  <div className="flex w-full items-center justify-center">
                <div className="w-full h-40 bg-gray-100 rounded bg-center bg-cover flex items-center justify-center">Image</div>
              </div>

</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  )
}
